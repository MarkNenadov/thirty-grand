import pytest
from unittest.mock import Mock
from src.thirty_grand import observation
from thirty_grand.utilities.tables import get_property_distinct_species_count


@pytest.fixture
def observations():
    observation1 = Mock(spec=observation.Observation)
    observation1.order_name = "Lepidoptera"
    observation1.scientific_name = "Actias lunas"
    observation1.observed_on = "2023-05-25"

    observation2 = Mock(spec=observation.Observation)
    observation2.order_name = "Orthoptera"
    observation2.scientific_name = "Something something"
    observation2.observed_on = "2023-05-26"

    observation3 = Mock(spec=observation.Observation)
    observation3.order_name = "Lepidoptera"
    observation3.scientific_name = "Actias"
    observation3.observed_on = "2022-04-15"

    return [observation1, observation2, observation3]


def test_get_property_distinct_species_count_when_one(observations):
    count = get_property_distinct_species_count("order_name", "Lepidoptera", observations)

    assert count == 1


def test_get_property_distinct_species_count_when_none(observations):
    count = get_property_distinct_species_count("order_name", "Coleoptera", observations)

    assert count == 0


if __name__ == '__main__':
    pytest.main()
