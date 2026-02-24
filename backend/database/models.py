from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

from core.enums import PayoutType


class Influencer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    payouts: list["Payout"] = Relationship(
        back_populates="influencer", cascade_delete=True
    )


class OfferCategoryLink(SQLModel, table=True):
    offer_id: int = Field(foreign_key="offer.id", primary_key=True)
    category_id: int = Field(foreign_key="category.id", primary_key=True)


class Category(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True)

    offers: list["Offer"] = Relationship(
        back_populates="categories",
        link_model=OfferCategoryLink,
    )


class Payout(SQLModel, table=True):
    __table_args__ = (UniqueConstraint("offer_id", "influencer_id"),)

    id: int = Field(default=None, primary_key=True)
    type: PayoutType
    cpa_amount: int | None = None
    fixed_amount: int | None = None

    offer_id: int = Field(foreign_key="offer.id", ondelete="CASCADE")
    offer: "Offer" = Relationship(back_populates="payouts")

    influencer_id: int | None = Field(
        default=None, foreign_key="influencer.id", ondelete="CASCADE"
    )
    influencer: Influencer | None = Relationship(back_populates="payouts")

    country_overrides: list["CountryOverride"] = Relationship(
        back_populates="payout", cascade_delete=True
    )


class CountryOverride(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    payout_id: int = Field(foreign_key="payout.id", ondelete="CASCADE")
    country_code: str = Field(max_length=2)
    cpa_amount: int

    payout: Payout = Relationship(back_populates="country_overrides")


class Offer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=50)
    description: str = Field(max_length=100)

    payouts: list["Payout"] = Relationship(
        back_populates="offer",
        cascade_delete=True,
    )

    categories: list[Category] = Relationship(
        back_populates="offers",
        link_model=OfferCategoryLink,
    )

    @property
    def payout(self) -> "Payout | None":
        return next((p for p in self.payouts if p.influencer_id is None), None)
