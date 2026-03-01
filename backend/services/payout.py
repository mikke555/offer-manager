from api.schemas.payout import PayoutCreate, PayoutResp
from core.exceptions import (
    DefaultPayoutDeletionException,
    InfluencerNotFoundException,
    NotFoundException,
    PayoutAlreadyExistsException,
)
from database.models import CountryOverride, Influencer, Payout
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from services.base import BaseService


class PayoutService(BaseService):
    model = Payout
    schema = PayoutResp
    name = "Payout"

    def __init__(self, session: Session):
        self.session = session

    def _create(
        self, offer_id: int, payout: PayoutCreate, influencer_id: int | None = None
    ) -> Payout:
        db_payout = Payout(
            type=payout.type,
            cpa_amount=payout.cpa_amount,
            fixed_amount=payout.fixed_amount,
            offer_id=offer_id,
            influencer_id=influencer_id,
        )
        self.session.add(db_payout)
        self.session.flush()

        for override in payout.country_overrides:
            db_override = CountryOverride(
                payout_id=db_payout.id,
                country_code=override.country_code,
                cpa_amount=override.cpa_amount,
            )
            self.session.add(db_override)

        return db_payout

    def list(self, offer_id: int) -> list[PayoutResp]:
        return self.list_by(selectinload(Payout.country_overrides), offer_id=offer_id)

    def create_default(self, offer_id: int, payout: PayoutCreate) -> None:
        self._create(offer_id, payout)

    def replace_default(self, offer_id: int, payout: PayoutCreate) -> None:
        existing = self.session.exec(
            select(Payout).where(
                Payout.offer_id == offer_id, Payout.influencer_id.is_(None)
            )
        ).first()

        if existing:
            self.session.delete(existing)
            self.session.flush()
        self._create(offer_id, payout)

    def add(self, offer_id: int, payout: PayoutCreate) -> PayoutResp:
        if payout.influencer_id is not None:
            if not self.session.get(Influencer, payout.influencer_id):
                raise InfluencerNotFoundException(id=payout.influencer_id)

        if self.session.exec(
            select(Payout).where(
                Payout.offer_id == offer_id,
                Payout.influencer_id == payout.influencer_id,
            )
        ).first():
            raise PayoutAlreadyExistsException(offer_id, payout.influencer_id)

        db_payout = self._create(offer_id, payout, payout.influencer_id)
        self.session.commit()
        self.session.refresh(db_payout)
        return PayoutResp.model_validate(db_payout)

    def update(self, offer_id: int, payout_id: int, payout: PayoutCreate) -> PayoutResp:
        db_payout = self.session.get(Payout, payout_id)
        if not db_payout or db_payout.offer_id != offer_id:
            raise NotFoundException(id=payout_id, name="Payout")

        self.session.delete(db_payout)
        self.session.flush()

        db_payout = self._create(offer_id, payout, db_payout.influencer_id)
        self.session.commit()
        self.session.refresh(db_payout)
        return PayoutResp.model_validate(db_payout)

    def remove(self, offer_id: int, payout_id: int) -> None:
        db_payout = self.session.get(Payout, payout_id)
        if not db_payout or db_payout.offer_id != offer_id:
            raise NotFoundException(id=payout_id, name="Payout")

        if db_payout.influencer_id is None:
            raise DefaultPayoutDeletionException()

        self.session.delete(db_payout)
        self.session.commit()
