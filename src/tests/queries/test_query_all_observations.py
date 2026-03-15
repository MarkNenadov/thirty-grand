import pandas as pd
import pytest

from thirty_grand.queries import query_all_observations


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


def test_query_all_observations_returns_all_rows(data) -> None:
    result = query_all_observations(data)
    assert len(result) == 3


def test_query_all_observations_returns_empty_list_for_empty_dataframe() -> None:
    result = query_all_observations(pd.DataFrame())
    assert result == []


def test_query_all_observations_filters_by_scientific_name_partial(data) -> None:
    result = query_all_observations(data, scientific_name_partial="luna")
    assert len(result) == 1
    assert result[0].scientific_name == "Actias luna"


def test_query_all_observations_filters_by_common_name_partial(data) -> None:
    result = query_all_observations(data, common_name_partial="moth")
    assert len(result) == 1
    assert result[0].common_name == "Luna Moth"


def test_query_all_observations_filters_by_both_partials(data) -> None:
    result = query_all_observations(data, scientific_name_partial="Actias", common_name_partial="moth")
    assert len(result) == 1
    assert result[0].scientific_name == "Actias luna"


def test_query_all_observations_returns_empty_list_when_no_match(data) -> None:
    result = query_all_observations(data, scientific_name_partial="Ursus")
    assert result == []
