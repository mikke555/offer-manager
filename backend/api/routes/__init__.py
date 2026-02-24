from fastapi import APIRouter

from api.routes.category import router as category_router
from api.routes.influencer import router as influencer_router
from api.routes.offer import router as offer_router
from api.routes.payout import router as payout_router

master_router = APIRouter(prefix="/api")

master_router.include_router(offer_router)
master_router.include_router(payout_router)
master_router.include_router(category_router)
master_router.include_router(influencer_router)
