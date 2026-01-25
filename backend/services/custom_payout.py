from api.schemas.payout import CustomPayoutCreate, CustomPayoutResp
from core.exceptions import (
    CustomPayoutAlreadyExistsException,
    InfluencerNotFoundException,
)
from database.models import CustomCountryOverride, CustomPayout, Influencer
from sqlalchemy.orm import selectinload

from services.base import BaseService


class CustomPayoutService(BaseService):
    model = CustomPayout
    schema = CustomPayoutResp
    name = "Custom Payout"

    def _append_custom_payout(
        self, offer_id: int, influencer_id: int, payout: CustomPayoutCreate
    ) -> CustomPayout:
        db_custom_payout = CustomPayout(
            offer_id=offer_id,
            influencer_id=influencer_id,
            type=payout.type,
            cpa_amount=payout.cpa_amount,
            fixed_amount=payout.fixed_amount,
        )
        self.session.add(db_custom_payout)
        self.session.flush()

        for override in payout.country_overrides:
            db_override = CustomCountryOverride(
                custom_payout_id=db_custom_payout.id,
                country_code=override.country_code,
                cpa_amount=override.cpa_amount,
            )
            self.session.add(db_override)

        return db_custom_payout

    def list(self, offer_id: int) -> list[CustomPayoutResp]:
        return self.list_by(
            selectinload(CustomPayout.country_overrides), offer_id=offer_id
        )

    def get(self, offer_id: int, influencer_id: int) -> CustomPayoutResp:
        db_custom_payout = self.get_by(offer_id=offer_id, influencer_id=influencer_id)
        return CustomPayoutResp.model_validate(db_custom_payout)

    def add(
        self, offer_id: int, influencer_id: int, payout: CustomPayoutCreate
    ) -> CustomPayoutResp:
        if not self.session.get(Influencer, influencer_id):
            raise InfluencerNotFoundException(id=influencer_id)

        if self.exists(offer_id=offer_id, influencer_id=influencer_id):
            raise CustomPayoutAlreadyExistsException(offer_id, influencer_id)

        db_custom_payout = self._append_custom_payout(offer_id, influencer_id, payout)

        self.session.commit()
        self.session.refresh(db_custom_payout)
        return CustomPayoutResp.model_validate(db_custom_payout)

    def update(
        self, offer_id: int, influencer_id: int, payout: CustomPayoutCreate
    ) -> CustomPayoutResp:
        db_custom_payout = self._get_by(offer_id=offer_id, influencer_id=influencer_id)

        self.session.delete(db_custom_payout)
        self.session.flush()

        db_custom_payout = self._append_custom_payout(offer_id, influencer_id, payout)

        self.session.commit()
        self.session.refresh(db_custom_payout)
        return CustomPayoutResp.model_validate(db_custom_payout)

    def delete(self, offer_id: int, influencer_id: int):
        return self.delete_by(offer_id=offer_id, influencer_id=influencer_id)
