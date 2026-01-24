from fastapi import APIRouter

from api.routes.category import router as category_router
from api.routes.custom_payout import router as custom_payouts_router
from api.routes.influencer import router as influencer_router
from api.routes.offer import router as offer_router

master_router = APIRouter(prefix="/api")

master_router.include_router(offer_router)
master_router.include_router(custom_payouts_router)
master_router.include_router(category_router)
master_router.include_router(influencer_router)
