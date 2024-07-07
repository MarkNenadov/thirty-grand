from collections import Counter
import datetime

from src.thirty_grand import observation


def extract_years(observations: [observation.Observation]) -> []:
    return [datetime.datetime.strptime(obs.observed_on, "%Y-%m-%d").year for obs in observations]


def extract_yearly_observation_counts(observations: [observation.Observation]) -> [int, int]:
    year_counts = Counter(extract_years(observations))

    years = list(year_counts.keys())
    numbers = list(year_counts.values())

    return [years, numbers]
