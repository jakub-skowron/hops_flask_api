import pytest

from src import create_app, db
from config import TestingConfig


enpoint_prefix = "/api/v1"


def test_404(test_client):
    response = test_client.get(f"{enpoint_prefix}/hops/asdasd")
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"
    assert response.json["error"] == "page not found"


def test_405(test_client):
    response = test_client.patch(f"{enpoint_prefix}/hops/")
    assert response.status_code == 405
    assert response.headers["Content-Type"] == "application/json"
    assert response.json["error"] == "method not allowed"
