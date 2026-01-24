from fastapi import APIRouter
from sqlmodel import select

from api.deps import SessionDep
from api.schemas.category import CategoryResp
from database.models import Category

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/", response_model=list[CategoryResp])
def get_categories(session: SessionDep):
    return session.exec(select(Category)).all()
