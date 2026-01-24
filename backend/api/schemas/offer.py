from pydantic import BaseModel, ConfigDict, Field

from api.schemas.category import CategoryName, CategoryResp
from api.schemas.payout import PayoutCreate, PayoutResp


class OfferBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=100)


class OfferCreate(OfferBase):
    categories: list[CategoryName] | None = None
    payout: PayoutCreate


class OfferUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=50)
    description: str | None = Field(default=None, max_length=100)
    categories: list[CategoryName] | None = None
    payout: PayoutCreate | None = None


class OfferResp(OfferBase):
    id: int
    categories: list[CategoryResp] = []
    payout: PayoutResp

    model_config = ConfigDict(from_attributes=True)
