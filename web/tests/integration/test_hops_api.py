import json

import pytest

from src import create_app, db
from src.auth.models import User
from config import TestingConfig


enpoint_prefix = "/api/v1"

test_hop_payload = {
    "alpha_max_percentage": 15,
    "alpha_min_percentage": 10,
    "aroma": "citrus, grapefruit, lime, tropical fruits, harsh bitterness",
    "beer_styles": "India Pale Ale, American Ales, Amber",
    "beta_max_percentage": 4.5,
    "beta_min_percentage": 3,
    "description": "American aroma hop Citra was created by John I. Haas, Inc. and Select Botanicals Group joint venture, the Hop Breeding Company. It was released to the brewing world in 2008.",
    "name": "Citra",
    "origin": "US",
    "substitutions": "Simcoe, Cascade, Centennial, Mosaic",
    "used_for": "Bittering & Aroma",
}
test_hop_payload_2 = {
    "alpha_max_percentage": 15,
    "alpha_min_percentage": 10,
    "aroma": "citrus, grapefruit, lime, tropical fruits, harsh bitterness",
    "beer_styles": "India Pale Ale, American Ales, Amber",
    "beta_max_percentage": 4.5,
    "beta_min_percentage": 3,
    "description": "Lorem ipsum...",
    "name": "Mosaic",
    "origin": "US",
    "substitutions": "Simcoe, Cascade, Centennial, Citra",
    "used_for": "Bittering & Aroma",
}

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)

    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()
            email = "testuser@email.com"
            password = "testpass"
            user = User(email = email, password = password)
            user.hash_password(password)
            db.session.add(user)
            db.session.commit()

            yield test_client

            db.session.remove()
            db.drop_all()


def test_add_new_hop_with_valid_token(test_client):
    access_token = get_access_token(test_client)

    response = test_client.post(
        f"{enpoint_prefix}/hops/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(test_hop_payload),
    )

    response2 = test_client.post(
        f"{enpoint_prefix}/hops/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(test_hop_payload_2),
    )

    assert response.status_code == 201
    assert response2.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    assert response2.headers["Content-Type"] == "application/json"


def test_add_hop_with_invalid_token(test_client):
    access_token = get_access_token(test_client) + "invalid_suffix"

    response = test_client.post(
        f"{enpoint_prefix}/hops/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(test_hop_payload),
    )

    assert response.status_code == 422
    assert response.headers["Content-Type"] == "application/json"


def test_add_hop_which_already_exists(test_client):
    access_token = get_access_token(test_client)

    response = test_client.post(
        f"{enpoint_prefix}/hops/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps(test_hop_payload),
    )

    assert response.status_code == 409
    assert response.headers["Content-Type"] == "application/json"


def test_get_all_hops(test_client):
    response = test_client.get(f"{enpoint_prefix}/hops/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_all_hops_with_query_strings(test_client):
    query_params = {
        "per_page": 2,
        "beta_max_percentage": 4.5
        }
    response = test_client.get(f"{enpoint_prefix}/hops/", query_string=query_params)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_all_hops_with_partly_query_string_value(test_client):
    query_params = {
        "origin": "U"
        }
    response = test_client.get(f"{enpoint_prefix}/hops/", query_string=query_params)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_hop_by_id(test_client, id=1):
    response = test_client.get(f"{enpoint_prefix}/hops/{id}/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_get_hop_by_id_with_invalid_id(test_client, id=5):
    response = test_client.get(f"{enpoint_prefix}/hops/{id}/")
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"


def test_get_random_hop(test_client):
    response = test_client.get(f"{enpoint_prefix}/hops/random/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_update_hop_with_valid_token(test_client, id=1):
    access_token = get_access_token(test_client)

    response = test_client.put(
        f"{enpoint_prefix}/hops/{id}/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps({"origin": "PL"}),
    )

    assert response.status_code == 202
    assert response.headers["Content-Type"] == "application/json"
    assert json.loads(response.data)["origin"] == "PL"


def test_update_hop_existed_name(test_client, id=1):
    access_token = get_access_token(test_client)

    response = test_client.put(
        f"{enpoint_prefix}/hops/{id}/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
        data=json.dumps({"name": "Mosaic"}),
    )

    assert response.status_code == 409
    assert response.headers["Content-Type"] == "application/json"


def test_delete_hop_with_valid_token(test_client, id=1):
    access_token = get_access_token(test_client)
    response = test_client.delete(
        f"{enpoint_prefix}/hops/{id}/",
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        },
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def get_access_token(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/login/",
        data=json.dumps({"email": "testuser@email.com", "password": "testpass"}),
        headers={"Content-Type": "application/json"},
    )
    access_token = json.loads(response.data)["user"]["access"]
    return access_token
