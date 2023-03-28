import pytest

from config import TestingConfig
from src import create_app, db


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)

    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()
            yield test_client

            db.session.remove()
            db.drop_all()
