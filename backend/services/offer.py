from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from api.schemas.offer import OfferCreate, OfferResp, OfferUpdate
from api.schemas.payout import PayoutCreate, PayoutResp
from core.exceptions import InfluencerNotFoundException, InvalidCategoryException
from database.models import (
    Category,
    CountryOverride,
    CustomPayout,
    Influencer,
    Offer,
    Payout,
)
from services.base import BaseService


class OfferService(BaseService):
    model = Offer
    schema = OfferResp

    def __init__(self, session: Session):
        self.session = session

    def _append_categories(self, db_offer: Offer, categories: list[str]) -> None:
        statement = select(Category).where(Category.name.in_(categories))
        db_categories = self.session.exec(statement).all()

        if len(db_categories) != len(categories):
            raise InvalidCategoryException()

        db_offer.categories.clear()
        db_offer.categories.extend(db_categories)

    def _append_payout(self, db_offer: Offer, payout: PayoutCreate) -> None:
        db_payout = Payout(
            type=payout.type,
            cpa_amount=payout.cpa_amount,
            fixed_amount=payout.fixed_amount,
            offer_id=db_offer.id,
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

    def list(
        self, offset: int = 0, limit: int = 20, influencer_id: int | None = None
    ) -> list[OfferResp]:
        if influencer_id is not None and not self.session.get(
            Influencer, influencer_id
        ):
            raise InfluencerNotFoundException()

        statement = (
            select(Offer)
            .options(
                selectinload(Offer.categories),
                selectinload(Offer.payout).selectinload(Payout.country_overrides),
            )
            .offset(offset)
            .limit(limit)
        )
        offers = self.session.exec(statement).all()

        if influencer_id is None:
            return [OfferResp.model_validate(offer) for offer in offers]

        offer_ids = [offer.id for offer in offers]
        custom_statement = (
            select(CustomPayout)
            .options(selectinload(CustomPayout.country_overrides))
            .where(
                CustomPayout.offer_id.in_(offer_ids),
                CustomPayout.influencer_id == influencer_id,
            )
        )
        custom_payouts = {
            cp.offer_id: cp for cp in self.session.exec(custom_statement).all()
        }

        personalized_offers = []
        for offer in offers:
            offer_resp = OfferResp.model_validate(offer)
            if custom_payout := custom_payouts.get(offer.id):
                offer_resp.payout = PayoutResp.model_validate(custom_payout)
            personalized_offers.append(offer_resp)

        return personalized_offers

    def add(self, offer: OfferCreate) -> OfferResp:
        db_offer = Offer(title=offer.title, description=offer.description)

        if offer.categories:
            self._append_categories(db_offer, offer.categories)

        self.session.add(db_offer)
        self.session.flush()

        self._append_payout(db_offer, offer.payout)

        self.session.commit()
        self.session.refresh(db_offer)
        return OfferResp.model_validate(db_offer)

    def update(self, id: int, offer: OfferUpdate) -> OfferResp:
        db_offer = self._get(id)

        db_offer.sqlmodel_update(
            offer.model_dump(
                exclude_unset=True,
                exclude={"categories", "payout"},
            )
        )

        if offer.categories:
            self._append_categories(db_offer, offer.categories)

        if offer.payout is not None:
            if db_offer.payout:
                self.session.delete(db_offer.payout)
                self.session.flush()
            self._append_payout(db_offer, offer.payout)

        self.session.commit()
        self.session.refresh(db_offer)
        return OfferResp.model_validate(db_offer)
