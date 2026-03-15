import pandas as pd
import pytest

from thirty_grand.queries import random_sample


@pytest.fixture
def data() -> pd.DataFrame:
    return pd.DataFrame({
        'id': [1, 2, 3],
        'observed_on_string': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'observed_on': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'time_observed_at': ['', '', ''],
        'taxon_class_name': ['Insecta', 'Insecta', 'Insecta'],
        'taxon_order_name': ['Lepidoptera', 'Lepidoptera', 'Lepidoptera'],
        'taxon_family_name': ['Papilionidae', 'Papilionidae', 'Papilionidae'],
        'scientific_name': ['Actias luna', 'Papilio glaucus', 'Pieris rapae'],
        'common_name': ['Luna Moth', 'Tiger Swallowtail', 'Cabbage White'],
        'place_guess': ['Ontario', 'Ontario', 'Ontario'],
        'iconic_taxon_name': ['Insecta', 'Insecta', 'Insecta'],
        'taxon_id': [1, 2, 3],
        'longitude': ['0.0', '0.0', '0.0'],
        'latitude': ['0.0', '0.0', '0.0'],
        'image_url': ['', '', ''],
    })


def test_random_sample_returns_correct_count(data) -> None:
    result = random_sample(data, 2)
    assert len(result) == 2


def test_random_sample_raises_when_count_exceeds_population(data) -> None:
    with pytest.raises(ValueError):
        random_sample(data, 10)
