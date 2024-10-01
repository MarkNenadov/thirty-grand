from collections import Counter
from typing import List, Tuple

from thirty_grand.observation import Observation


def is_probable_species(scientific_name: str) -> bool:
    if (scientific_name is None):
        return False
    split_by_species = scientific_name.split(" ")
    return len(split_by_species) >= 2 and len(split_by_species) < 4


def extract_years(observations: [Observation]) -> List[int]:
    """
    Extract year ints from a list of observations.

    Parameters:
        observations: The list of observations.
    """
    assert len(observations) > 0
    return [obs.get_year() for obs in observations if obs.observed_on != '']


def extract_yearly_observation_counts(observations: [Observation]) -> Tuple[List[int], List[int]]:
    """
    Extract a tuple of years with their counts from a list of observations.

    Parameters:
        observations: The list of observations.
    """
    assert len(observations) > 0
    year_counts = Counter(extract_years(observations))

    years, counts = zip(*year_counts.items())

    return years, counts
