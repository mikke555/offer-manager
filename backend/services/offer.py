from api.schemas.offer import OfferCreate, OfferResp, OfferUpdate
from api.schemas.payout import PayoutResp
from core.exceptions import InfluencerNotFoundException, InvalidCategoryException
from database.models import Category, Influencer, Offer, Payout
from services.base import BaseService
from services.payout import PayoutService
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select


class OfferService(BaseService):
    model = Offer
    schema = OfferResp
    name = "Offer"

    def __init__(self, session: Session):
        self.session = session
        self.payout_service = PayoutService(session)

    def _append_categories(self, db_offer: Offer, categories: list[str]) -> None:
        statement = select(Category).where(Category.name.in_(categories))
        db_categories = self.session.exec(statement).all()

        if len(db_categories) != len(categories):
            raise InvalidCategoryException()

        db_offer.categories.clear()
        db_offer.categories.extend(db_categories)

    def list(
        self, offset: int = 0, limit: int = 20, influencer_id: int | None = None
    ) -> list[OfferResp]:
        if influencer_id is not None and not self.session.get(
            Influencer, influencer_id
        ):
            raise InfluencerNotFoundException(id=influencer_id)

        statement = (
            select(Offer)
            .options(
                selectinload(Offer.categories),
                selectinload(Offer.payouts).selectinload(Payout.country_overrides),
            )
            .offset(offset)
            .limit(limit)
        )
        offers = self.session.exec(statement).all()

        offer_list = []
        for offer in offers:
            offer_resp = OfferResp.model_validate(offer)
            if influencer_id is not None:
                custom = next(
                    (p for p in offer.payouts if p.influencer_id == influencer_id),
                    None,
                )
                if custom:
                    offer_resp.payout = PayoutResp.model_validate(custom)
            offer_list.append(offer_resp)

        return offer_list

    def add(self, offer: OfferCreate) -> OfferResp:
        db_offer = Offer(title=offer.title, description=offer.description)

        if offer.categories:
            self._append_categories(db_offer, offer.categories)

        self.session.add(db_offer)
        self.session.flush()

        self.payout_service.create_default(db_offer.id, offer.payout)

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
            self.payout_service.replace_default(db_offer.id, offer.payout)

        self.session.commit()
        self.session.refresh(db_offer)
        return OfferResp.model_validate(db_offer)
