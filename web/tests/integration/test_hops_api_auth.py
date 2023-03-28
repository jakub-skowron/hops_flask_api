import json

import pytest

from src import create_app, db
from config import TestingConfig


enpoint_prefix = "/api/v1"


def test_create_user(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/register/",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"email": "testuser@email.com", "password": "testpass"}),
    )

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"


def test_create_user_without_password(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/register/",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"email": "testuser@email.com", "password": ""}),
    )

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"


def test_create_user_with_existed_email(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/register/",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"email": "testuser@email.com", "password": "testpassword2"}),
    )

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"


def test_login(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/login/",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"email": "testuser@email.com", "password": "testpass"}),
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"


def test_login_with_invalid_payload(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/login/",
        headers={
            "Content-Type": "application/json",
        },
        data=json.dumps({"email": "testuser@email.com", "password": ""}),
    )

    assert response.status_code == 401
    assert response.headers["Content-Type"] == "application/json"


def test_token_refresh(test_client):
    refresh_token = get_refresh_token(test_client)
    response = test_client.get(
        f"{enpoint_prefix}/auth/token/refresh/",
        headers={
            "Authorization": f"Bearer {refresh_token}",
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


def get_refresh_token(test_client):
    response = test_client.post(
        f"{enpoint_prefix}/auth/login/",
        data=json.dumps({"email": "testuser@email.com", "password": "testpass"}),
        headers={"Content-Type": "application/json"},
    )
    access_token = json.loads(response.data)["user"]["refresh"]
    return access_token
