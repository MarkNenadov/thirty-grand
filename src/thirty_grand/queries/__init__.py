import random
from typing import Optional

import pandas as pd

from .. import observation


def _name_matches(partial: Optional[str], full_name: str) -> bool:
    return partial is None or (isinstance(full_name, str) and partial.lower() in full_name.lower())


def query_all_observations(
        data: pd.DataFrame,
        scientific_name_partial: Optional[str] = None,
        common_name_partial: Optional[str] = None
) -> [observation.Observation]:
    """
    Query all observations from a DataFrame returned from csv. Optionally, match the given partial
    scientific and common names.

    Args:
        data (pd.DataFrame): The DataFrame containing observation csv data.
        scientific_name_partial (Optional[str]): Partial latin/scientific name to filter observations.
        common_name_partial (Optional[str]): Partial common name to filter observations.

    Returns:
        List[observation.Observation]: A list of Observation objects that match the given partial names.
    """
    observations = []
    for _, row in data.iterrows():
        if _name_matches(common_name_partial, row['common_name']) and \
                _name_matches(scientific_name_partial, row['scientific_name']):
            observations.append(observation.Observation.create_from_row(row))
    return observations


def random_sample(data: pd.DataFrame, count: int):
    """
    Retrieve a random sample of observations from the DataFrame.

    Args:
        data (pd.DataFrame): The DataFrame containing observation csv data.
        count (int): The number of random observations to retrieve.

    Returns:
        List[observation.Observation]: A random sample of Observation objects.
    """
    return random.sample(query_all_observations(data), count)
