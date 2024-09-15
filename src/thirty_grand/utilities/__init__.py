from collections import Counter
import datetime
from typing import List, Tuple

from src.thirty_grand import observation


def extract_years(observations: [observation.Observation]) -> List[int]:
    """
    Extract year ints from a list of observations.

    Parameters:
        observations: The list of observations.
    """
    return [obs.get_year() for obs in observations if obs.observed_on != '']


def extract_yearly_observation_counts(observations: [observation.Observation]) -> Tuple[List[int], List[int]]:
    """
    Extract a tuple of years with their counts from a list of observations.

    Parameters:
        observations: The list of observations.
    """
    year_counts = Counter(extract_years(observations))

    years, counts = zip(*year_counts.items())

    return years, counts
