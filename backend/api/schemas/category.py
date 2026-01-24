from pydantic import BaseModel, ConfigDict

from core.enums import CategoryName


class CategoryBase(BaseModel):
    name: CategoryName


class CategoryResp(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
