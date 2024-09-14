import pytest
from unittest.mock import Mock
from src.thirty_grand import observation
from src.thirty_grand.utilities import extract_yearly_observation_counts

@pytest.fixture
def observations():
    observation1 = Mock(spec=observation.Observation)
    observation1.observed_on = "2023-05-25"

    observation2 = Mock(spec=observation.Observation)
    observation2.observed_on = "2023-05-26"

    observation3 = Mock(spec=observation.Observation)
    observation3.observed_on = "2022-04-15"

    return [observation1, observation2, observation3]


def test_extract_yearly_observation_counts(observations):
    expected_years = (2023, 2022)
    expected_counts = (2, 1)

    years, counts = extract_yearly_observation_counts(observations)

    assert years == expected_years
    assert counts == expected_counts


if __name__ == '__main__':
    pytest.main()
