from fastapi import APIRouter
from sqlmodel import select

from api.deps import SessionDep
from api.schemas.influencer import InfluencerResp
from database.models import Influencer

router = APIRouter(prefix="/influencers", tags=["Influencers"])


@router.get("/", response_model=list[InfluencerResp])
def get_categories(session: SessionDep):
    return session.exec(select(Influencer)).all()
