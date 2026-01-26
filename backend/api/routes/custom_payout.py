from fastapi import APIRouter, status, Body

from api.deps import CustomPayoutServiceDep, OfferDep
from api.schemas.payout import CustomPayoutCreate, CustomPayoutResp
from api.const import custom_payout_put_examples


router = APIRouter(prefix="/offers", tags=["Custom Payouts"])


@router.get("/{offer_id}/custom-payouts", response_model=list[CustomPayoutResp])
def get_custom_payouts(offer: OfferDep, custom_payout_service: CustomPayoutServiceDep):
    return custom_payout_service.list(offer.id)


@router.post(
    "/{offer_id}/custom-payouts",
    response_model=CustomPayoutResp,
    status_code=status.HTTP_201_CREATED,
)
def create_custom_payout(
    offer: OfferDep,
    influencer_id: int,
    payout: CustomPayoutCreate,
    custom_payout_service: CustomPayoutServiceDep,
):
    return custom_payout_service.add(offer.id, influencer_id, payout)


@router.get(
    "/{offer_id}/custom-payouts/{influencer_id}", response_model=CustomPayoutResp
)
def get_custom_payout(
    offer: OfferDep, influencer_id: int, custom_payout_service: CustomPayoutServiceDep
):
    return custom_payout_service.get(offer.id, influencer_id)


@router.put(
    "/{offer_id}/custom-payouts/{influencer_id}", response_model=CustomPayoutResp
)
def update_custom_payout(
    *,
    offer: OfferDep,
    influencer_id: int,
    payout: CustomPayoutCreate = Body(openapi_examples=custom_payout_put_examples),
    custom_payout_service: CustomPayoutServiceDep,
):
    return custom_payout_service.update(offer.id, influencer_id, payout)


@router.delete(
    "/{offer_id}/custom-payouts/{influencer_id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_custom_payout(
    offer: OfferDep, influencer_id: int, custom_payout_service: CustomPayoutServiceDep
):
    return custom_payout_service.delete(offer.id, influencer_id)
