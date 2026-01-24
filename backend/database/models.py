from sqlmodel import Field, Relationship, SQLModel

from core.enums import PayoutType


class Influencer(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str

    custom_payouts: list["CustomPayout"] = Relationship(
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
    id: int = Field(default=None, primary_key=True)
    type: PayoutType
    cpa_amount: int | None = None
    fixed_amount: int | None = None

    offer_id: int = Field(foreign_key="offer.id", unique=True)
    offer: "Offer" = Relationship(back_populates="payout")

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

    payout: "Payout" = Relationship(
        back_populates="offer",
        sa_relationship_kwargs={
            "uselist": False,  # one-to-one rel
            "cascade": "all,delete,delete-orphan",
        },
    )

    categories: list[Category] = Relationship(
        back_populates="offers",
        link_model=OfferCategoryLink,
    )

    custom_payouts: list["CustomPayout"] = Relationship(
        back_populates="offer", cascade_delete=True
    )


class CustomCountryOverride(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    custom_payout_id: int = Field(foreign_key="custompayout.id", ondelete="CASCADE")
    country_code: str = Field(max_length=2)
    cpa_amount: int

    custom_payout: "CustomPayout" = Relationship(back_populates="country_overrides")


class CustomPayout(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    offer_id: int = Field(foreign_key="offer.id", ondelete="CASCADE")
    influencer_id: int = Field(foreign_key="influencer.id", ondelete="CASCADE")
    type: PayoutType
    cpa_amount: int | None = None
    fixed_amount: int | None = None

    offer: Offer = Relationship(back_populates="custom_payouts")
    influencer: Influencer = Relationship(back_populates="custom_payouts")
    country_overrides: list[CustomCountryOverride] = Relationship(
        back_populates="custom_payout", cascade_delete=True
    )
