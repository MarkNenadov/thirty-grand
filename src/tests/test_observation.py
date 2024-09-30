import pytest
from datetime import datetime
from src.thirty_grand.observation import Observation

@pytest.fixture
def observation_data():
    return {
        'obs_id': 1,
        'observed_on_string': '2023-05-25',
        'observed_on': '2023-05-25',
        'time_observed_at': '2023-05-25T14:30:00Z',
        'taxon_class_name': 'Class',
        'taxon_order_name': 'Order',
        'taxon_family_name': 'Family',
        'scientific_name': 'Panthera leo',
        'common_name': 'Lion',
        'place_guess': 'Bengal',
        'iconic_taxon_name': 'Mammalia',
        'taxon_id': 12345
    }

@pytest.fixture
def observation(observation_data):
    data = observation_data
    return Observation(
        data['obs_id'],
        data['observed_on_string'],
        data['observed_on'],
        data['time_observed_at'],
        data['taxon_class_name'],
        data['taxon_order_name'],
        data['taxon_family_name'],
        data['scientific_name'],
        data['common_name'],
        data['place_guess'],
        data['iconic_taxon_name'],
        data['taxon_id'],
        data['longitude'],
        data['latitude'],
        data['image_url'],
    )


def test_constructor(observation, observation_data):
    data = observation_data
    assert observation.obs_id == data['obs_id']
    assert observation.observed_on_string == data['observed_on_string']
    assert observation.observed_on == data['observed_on']
    assert observation.time_observed_at == data['time_observed_at']
    assert observation.class_name == data['taxon_class_name']
    assert observation.order_name == data['taxon_order_name']
    assert observation.family_name == data['taxon_family_name']
    assert observation.scientific_name == data['scientific_name']
    assert observation.common_name == data['common_name']
    assert observation.place_guess == data['place_guess']
    assert observation.iconic_taxon_name == data['iconic_taxon_name']
    assert observation.taxon_id == data['taxon_id']
    assert observation.longitude == data['longitude']
    assert observation.latitude == data['latitude']
    assert observation.image_url == data['image_url']


def test_get_year(observation):
    assert observation.get_year() == 2023

def test_repr(observation):
    expected_repr = (
        "Observation(obs_id=1, "
        "observed_on_string='2023-05-25', "
        "observed_on='2023-05-25', "
        "time_observed_at='2023-05-25T14:30:00Z', "
        "class_name='Class', "
        "order_name='Order', "
        "family_name='Family', "
        "scientific_name='Panthera leo', "
        "common_name='Lion', "
        "place_guess='Bengal', "
        "iconic_taxon_name='Mammalia', "
        "taxon_id=12345)"
    )
    assert repr(observation) == expected_repr


def test_create_from_row():
    row = {
        'id': 2,
        'observed_on_string': '2023-05-26',
        'observed_on': '2023-05-26',
        'time_observed_at': '2023-05-26T14:30:00Z',
        'scientific_name': 'Panthera tigris',
        'taxon_class_name': 'Class',
        'taxon_order_name': 'Order',
        'taxon_family_name': 'Family',
        'common_name': 'Tiger',
        'place_guess': "Bengal",
        'iconic_taxon_name': 'Mammalia',
        'taxon_id': 67890,
        'longitude':"34343",
        'latitude': "-34343",
        'image_url': 'https://www.test.com/',
    }
    obs = Observation.create_from_row(row)
    assert obs.obs_id == row['id']
    assert obs.observed_on_string == row['observed_on_string']
    assert obs.observed_on == row['observed_on']
    assert obs.time_observed_at == row['time_observed_at']
    assert obs.scientific_name == row['scientific_name']
    assert obs.common_name == row['common_name']
    assert obs.place_guess == row['place_guess']
    assert obs.iconic_taxon_name == row['iconic_taxon_name']
    assert obs.taxon_id == row['taxon_id']


if __name__ == '__main__':
    pytest.main()
