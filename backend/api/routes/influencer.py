from fastapi import APIRouter
from sqlmodel import select

from api.deps import SessionDep
from api.schemas.influencer import InfluencerResp
from database.models import Influencer
from core.exceptions import InfluencerNotFoundException

router = APIRouter(prefix="/influencers", tags=["Influencers"])


@router.get("/", response_model=list[InfluencerResp])
def get_influencers(session: SessionDep):
    return session.exec(select(Influencer)).all()


@router.get("/{influencer_id}", response_model=InfluencerResp)
def get_influencer(influencer_id: int, session: SessionDep):
    db_influencer = session.get(Influencer, influencer_id)
    if not db_influencer:
        raise InfluencerNotFoundException(id=influencer_id)
    return db_influencer
