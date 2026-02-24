from pydantic import BaseModel, ConfigDict, Field, model_validator

from database.models import PayoutType


class CountryOverrideBase(BaseModel):
    country_code: str = Field(min_length=2, max_length=2)
    cpa_amount: int = Field(gt=0)


class CountryOverrideCreate(CountryOverrideBase):
    pass


class CountryOverrideResp(CountryOverrideBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class PayoutBase(BaseModel):
    type: PayoutType
    cpa_amount: int | None = None
    fixed_amount: int | None = None

    @model_validator(mode="after")
    def validate_amounts(self):
        match self.type:
            case PayoutType.CPA:
                if not self.cpa_amount or self.cpa_amount <= 0:
                    raise ValueError("cpa_amount must be positive for CPA payout")
            case PayoutType.FIXED:
                if not self.fixed_amount or self.fixed_amount <= 0:
                    raise ValueError("fixed_amount must be positive for FIXED payout")
            case PayoutType.CPA_FIXED:
                if not self.cpa_amount or self.cpa_amount <= 0:
                    raise ValueError("cpa_amount must be positive for CPA_FIXED payout")
                if not self.fixed_amount or self.fixed_amount <= 0:
                    raise ValueError(
                        "fixed_amount must be positive for CPA_FIXED payout"
                    )
        return self


class PayoutCreate(PayoutBase):
    influencer_id: int | None = None
    country_overrides: list[CountryOverrideCreate] = []

    @model_validator(mode="after")
    def validate_country_overrides(self):
        if self.type == PayoutType.FIXED and self.country_overrides:
            raise ValueError("country_overrides not allowed for FIXED payout type")
        return self


class PayoutResp(PayoutBase):
    id: int
    influencer_id: int | None = None
    country_overrides: list[CountryOverrideResp] = []

    model_config = ConfigDict(from_attributes=True)
