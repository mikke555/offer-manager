from pydantic import BaseModel


class InfluencerBase(BaseModel):
    name: str


class InfluencerResp(InfluencerBase):
    id: int
