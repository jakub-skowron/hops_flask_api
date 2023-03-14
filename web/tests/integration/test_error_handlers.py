import pytest

from src import create_app, db
from config import TestingConfig


enpoint_prefix = "/api/v1"

@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)

    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()

            yield test_client

            db.session.remove()
            db.drop_all()


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

