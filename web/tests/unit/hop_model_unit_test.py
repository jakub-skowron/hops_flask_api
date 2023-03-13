import pytest

from src import create_app, db
from src.hops.models import Hop
from config import TestingConfig


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app(TestingConfig)

    with flask_app.test_client() as test_client:
        with flask_app.app_context():
            db.create_all()
            yield test_client

            db.session.remove()
            db.drop_all()


def test_add_hop(test_client):
    new_hop = Hop(
        name="test",
        alpha_max_percentage=12,
        alpha_min_percentage=10,
        beta_max_percentage=5,
        beta_min_percentage=4,
        origin="US",
        description="Lorem ipsum...",
        aroma="citrus",
        beer_styles="IPA, Lager",
        used_for="aroma",
        substitutions="test2",
    )
    db.session.add(new_hop)
    db.session.commit()

    hops = Hop.query.all()
    assert len(hops) == 1
    assert hops[0].name == "test"


def test_get_dict(test_client):
    hop = Hop.query.get(1)

    assert hop.as_dict() == {
        "id": 1,
        "name": "test",
        "alpha_max_percentage": 12,
        "alpha_min_percentage": 10,
        "beta_max_percentage": 5,
        "beta_min_percentage": 4,
        "origin": "US",
        "description": "Lorem ipsum...",
        "aroma": "citrus",
        "beer_styles": "IPA, Lager",
        "used_for": "aroma",
        "substitutions": "test2",
    }


def test_update_hop(test_client):
    hop = Hop.query.get(1)
    hop.name = "test_update"
    hop.origin = "PL"
    hop.alpha_max_percentage = 11
    db.session.commit()

    hops = Hop.query.all()
    assert len(hops) == 1
    assert hops[0].name == "test_update"
    assert hops[0].origin == "PL"
    assert hops[0].alpha_max_percentage == 11

    assert isinstance(hops[0].name, str)
    assert isinstance(hops[0].origin, str)
    assert isinstance(hops[0].alpha_max_percentage, int)


def test_delete_hop(test_client):
    hop = Hop.query.get(1)
    db.session.delete(hop)
    db.session.commit()

    hops = Hop.query.all()
    assert len(hops) == 0
