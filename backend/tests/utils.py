import json
from typing import Any

from sqlmodel import Session, select

from database.database import engine
from database.models import (
    Category,
    CountryOverride,
    CustomCountryOverride,
    CustomPayout,
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
        insert_offers(session, data["offers"])
        insert_custom_payouts(session, data["custom_payouts"])

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


def insert_offers(session: Session, data: list[dict[str, Any]]) -> None:
    records_exist = session.exec(select(Offer)).first()
    if records_exist:
        return

    categories = {c.name: c for c in session.exec(select(Category)).all()}
    offers: list[Offer] = []

    for item in data:
        payout_data = item["payout"]
        country_overrides = [
            CountryOverride(**override)
            for override in payout_data.get("country_overrides", [])
        ]

        payout = Payout(
            type=payout_data["type"],
            cpa_amount=payout_data.get("cpa_amount"),
            fixed_amount=payout_data.get("fixed_amount"),
            country_overrides=country_overrides,
        )

        offer_categories = [categories[name] for name in item["categories"]]

        offer = Offer(
            title=item["title"],
            description=item["description"],
            payout=payout,
            categories=offer_categories,
        )
        offers.append(offer)

    session.add_all(offers)
    session.flush()


def insert_custom_payouts(session: Session, data: list[dict[str, Any]]) -> None:
    records_exist = session.exec(select(CustomPayout)).first()
    if records_exist:
        return

    influencers = {i.name: i for i in session.exec(select(Influencer)).all()}
    offers_dict = {o.title: o for o in session.exec(select(Offer)).all()}

    custom_payouts: list[CustomPayout] = []

    for item in data:
        country_overrides = [
            CustomCountryOverride(**override)
            for override in item.get("country_overrides", [])
        ]

        custom_payout = CustomPayout(
            offer_id=offers_dict[item["offer_title"]].id,
            influencer_id=influencers[item["influencer_name"]].id,
            type=item["type"],
            cpa_amount=item.get("cpa_amount"),
            fixed_amount=item.get("fixed_amount"),
            country_overrides=country_overrides,
        )
        custom_payouts.append(custom_payout)

    session.add_all(custom_payouts)
    session.flush()
