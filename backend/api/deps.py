from typing import Annotated

from core.exceptions import OfferNotFoundException
from database.database import engine
from database.models import Offer
from fastapi import Depends
from services.custom_payout import CustomPayoutService
from services.offer import OfferService
from sqlmodel import Session


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


def get_offer(offer_id: int, session: SessionDep) -> Offer:
    offer = session.get(Offer, offer_id)
    if not offer:
        raise OfferNotFoundException(id=offer_id)
    return offer


OfferDep = Annotated[Offer, Depends(get_offer)]


def get_offer_service(session: SessionDep) -> OfferService:
    return OfferService(session)


OfferServiceDep = Annotated[OfferService, Depends(get_offer_service)]


def get_custom_payout_service(session: SessionDep) -> CustomPayoutService:
    return CustomPayoutService(session)


CustomPayoutServiceDep = Annotated[
    CustomPayoutService, Depends(get_custom_payout_service)
]
