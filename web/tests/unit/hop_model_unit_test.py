import pytest
from src import db
from src.hops.models import Hop


def create_hop():
    hop = Hop(
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
    db.session.add(hop)
    db.session.commit()
    return hop


@pytest.fixture
def hop_in_db():
    hop = create_hop()

    yield hop

    db.session.delete(hop)
    db.session.commit()


def test_add_hop(test_client, hop_in_db):
    expected_hop = Hop(
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
    hops = Hop.query.all()
    assert len(hops) == 1
    assert hops[0] == expected_hop


def test_get_dict(test_client, hop_in_db):
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


def test_update_hop(test_client, hop_in_db):
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
    create_hop()
    hop = Hop.query.get(1)
    db.session.delete(hop)
    db.session.commit()

    hops = Hop.query.all()
    assert len(hops) == 0
