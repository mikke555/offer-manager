from fastapi import APIRouter, status

from api.deps import PayoutServiceDep
from api.schemas.payout import PayoutCreate, PayoutResp

router = APIRouter(prefix="/offers", tags=["Payouts"])


@router.get("/{offer_id}/payouts", response_model=list[PayoutResp])
def get_payouts(offer_id: int, payout_service: PayoutServiceDep):
    return payout_service.list(offer_id)


@router.post(
    "/{offer_id}/payouts",
    response_model=PayoutResp,
    status_code=status.HTTP_201_CREATED,
)
def create_payout(
    offer_id: int, payout: PayoutCreate, payout_service: PayoutServiceDep
):
    return payout_service.add(offer_id, payout)


@router.put(
    "/{offer_id}/payouts/{payout_id}",
    response_model=PayoutResp,
)
def update_payout(
    offer_id: int,
    payout_id: int,
    payout: PayoutCreate,
    payout_service: PayoutServiceDep,
):
    return payout_service.update(offer_id, payout_id, payout)


@router.delete(
    "/{offer_id}/payouts/{payout_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_payout(offer_id: int, payout_id: int, payout_service: PayoutServiceDep):
    return payout_service.remove(offer_id, payout_id)
