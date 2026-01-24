from fastapi import APIRouter, Body, status

from api.const import offer_create_examples, offer_patch_examples
from api.deps import OfferServiceDep
from api.schemas.offer import OfferCreate, OfferResp, OfferUpdate

router = APIRouter(prefix="/offers", tags=["Offers"])


@router.get("/", response_model=list[OfferResp])
def get_offers(
    offer_service: OfferServiceDep,
    offset: int = 0,
    limit: int = 20,
    influencer_id: int | None = None,
):
    return offer_service.list(offset=offset, limit=limit, influencer_id=influencer_id)


@router.post("/", response_model=OfferResp, status_code=status.HTTP_201_CREATED)
def create_offer(
    *,
    offer: OfferCreate = Body(openapi_examples=offer_create_examples),
    offer_service: OfferServiceDep,
):
    return offer_service.add(offer)


@router.get("/{offer_id}", response_model=OfferResp)
def get_offer(offer_id: int, offer_service: OfferServiceDep):
    return offer_service.get(offer_id)


@router.patch("/{offer_id}", response_model=OfferResp)
def update_offer(
    *,
    offer_id: int,
    offer: OfferUpdate = Body(openapi_examples=offer_patch_examples),
    offer_service: OfferServiceDep,
):
    return offer_service.update(offer_id, offer)


@router.delete("/{offer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_offer(offer_id: int, offer_service: OfferServiceDep):
    return offer_service.delete(offer_id)
