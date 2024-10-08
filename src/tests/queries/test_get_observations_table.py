import pytest
from prettytable import PrettyTable
from unittest.mock import Mock

from thirty_grand.observation import Observation
from thirty_grand.utilities.tables import get_observations_table_str


@pytest.fixture
def observations() -> [Observation]:
    observation1 = Mock(spec=Observation)
    observation1.obs_id = 1
    observation1.observed_on_string = "2023-05-25"
    observation1.observed_on = "2023-05-25"
    observation1.time_observed_at = "10:00"
    observation1.scientific_name = "Panthera leo"
    observation1.common_name = "Lion"
    observation1.iconic_taxon_name = "Mammalia"
    observation1.taxon_id = 1234

    observation2 = Mock(spec=Observation)
    observation2.obs_id = 2
    observation2.observed_on_string = "2023-05-26"
    observation2.observed_on = "2023-05-26"
    observation2.time_observed_at = "12:00"
    observation2.scientific_name = "Elephas maximus"
    observation2.common_name = "Elephant"
    observation2.iconic_taxon_name = "Mammalia"
    observation2.taxon_id = 5678

    return [observation1, observation2]


def test_get_observations_table_str(observations) -> None:
    expected_table = PrettyTable()
    expected_table.field_names = [
        "Observation ID",
        "Observed On String",
        "Observed On",
        "Time Observed At",
        "Scientific Name",
        "Common Name",
        "Iconic Taxon Name",
    ]
    expected_table.add_row([
        1, "2023-05-25", "2023-05-25", "10:00", "Panthera leo", "Lion", "Mammalia"
    ])
    expected_table.add_row([
        2, "2023-05-26", "2023-05-26", "12:00", "Elephas maximus", "Elephant", "Mammalia"
    ])
    expected_output = expected_table.get_string()

    result = get_observations_table_str(observations)
    assert result == expected_output


if __name__ == '__main__':
    pytest.main()
