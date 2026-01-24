from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

TITLE_MAX_LENGTH = 50


def test_get_single_offer():
    resp = client.get("/api/offers/1")
    data = resp.json()

    assert resp.status_code == 200
    assert type(data) is dict
    assert data["title"]
    assert type(data["title"]) is str
    assert len(data["title"]) <= TITLE_MAX_LENGTH
