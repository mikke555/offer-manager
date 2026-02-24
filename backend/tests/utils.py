import json
from typing import Any

from sqlmodel import Session, select

from database.database import engine
from database.models import (
    Category,
    CountryOverride,
    Influencer,
    Offer,
    Payout,
)


def insert_dummy_data() -> None:
    with Session(engine) as session:
        with open("tests/mock_data.json") as file:
            data = json.load(file)

        insert_categories(session, data["categories"])
        insert_influencers(session, data["influencers"])
        insert_offers(session, data)

        session.commit()


def insert_categories(session: Session, data: list[str]) -> None:
    records_exist = session.exec(select(Category)).first()
    if records_exist:
        return

    session.add_all([Category(name=name) for name in data])
    session.flush()


def insert_influencers(session: Session, data: list[str]) -> None:
    records_exist = session.exec(select(Influencer)).first()
    if records_exist:
        return

    session.add_all([Influencer(name=name) for name in data])
    session.flush()


def insert_offers(session: Session, data: dict[str, Any]) -> None:
    records_exist = session.exec(select(Offer)).first()
    if records_exist:
        return

    categories = {c.name: c for c in session.exec(select(Category)).all()}
    influencers = {i.name: i for i in session.exec(select(Influencer)).all()}
    offers_by_title: dict[str, Offer] = {}

    for item in data["offers"]:
        payout = _build_payout(item["payout"])
        offer_categories = [categories[name] for name in item["categories"]]

        offer = Offer(
            title=item["title"],
            description=item["description"],
            payouts=[payout],
            categories=offer_categories,
        )
        offers_by_title[offer.title] = offer

    session.add_all(offers_by_title.values())
    session.flush()

    for item in data.get("custom_payouts", []):
        offer = offers_by_title[item["offer_title"]]
        influencer = influencers[item["influencer_name"]]
        payout = _build_payout(item, influencer_id=influencer.id)
        payout.offer_id = offer.id
        session.add(payout)

    session.flush()


def _build_payout(
    data: dict[str, Any], influencer_id: int | None = None
) -> Payout:
    country_overrides = [
        CountryOverride(**override)
        for override in data.get("country_overrides", [])
    ]
    return Payout(
        type=data["type"],
        cpa_amount=data.get("cpa_amount"),
        fixed_amount=data.get("fixed_amount"),
        influencer_id=influencer_id,
        country_overrides=country_overrides,
    )
