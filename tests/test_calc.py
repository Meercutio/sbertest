from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_valid_data():
    response = client.post(
        "/calc/",
        json={
              "date": "31.01.2022",
              "periods": 3,
              "amount": 10000,
              "rate": 6
            },
        )
    assert response.status_code == 200
    assert response.json() == {
            "31.01.2022": 10050,
            "28.02.2022": 10100.25,
            "31.03.2022": 10150.75
        }
