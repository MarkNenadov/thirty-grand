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
    observations = []
    for _, row in data.iterrows():
        if _name_matches(common_name_partial, row['common_name']) and _name_matches(scientific_name_partial, row['scientific_name']):
            observations.append(observation.Observation.create_from_row(row))
    return observations


def random_sample(data: pd.DataFrame, count: int):
    return random.sample(query_all_observations(data), count)
