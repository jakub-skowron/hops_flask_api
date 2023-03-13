import pytest

from src import create_app, db
from src.auth.models import User
from config import TestingConfig


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client

            db.session.remove()
            db.drop_all()


def test_create_user(test_client):
    user = User(email="test@test.pl", password="test123")
    user.hash_password(user.password)
    db.session.add(user)
    db.session.commit()

    users = User.query.all()
    assert len(users) == 1
    assert users[0].email == "test@test.pl"
    assert users[0].verify_password("test123")
