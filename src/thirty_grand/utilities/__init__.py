from prettytable import PrettyTable
from .. import observation
from collections import Counter
import datetime
import matplotlib.pyplot as pyplot


def get_observations_table_str(observations: [observation.Observation]):
    table = PrettyTable()
    table.field_names = [
        "Observation ID",
        "Observed On String",
        "Observed On",
        "Time Observed At",
        "Scientific Name",
        "Common Name",
        "Iconic Taxon Name",
        "Taxon ID"
    ]

    for obs in observations:
        table.add_row(
            [
                obs.obs_id,
                obs.observed_on_string,
                obs.observed_on,
                obs.time_observed_at,
                obs.scientific_name,
                obs.common_name,
                obs.iconic_taxon_name,
                obs.taxon_id
            ]
        )
    return table.get_string()


def print_observations_table(observations: [observation.Observation]) -> None:
    print(get_observations_table_str(observations))


def display_yearly_observation_barchart(observations: [observation.Observation]) -> None:
    years, numbers = extract_year_observation_counts(observations)

    pyplot.bar(years, numbers, color='skyblue')

    pyplot.title('Number of Observations Per Year')
    pyplot.xlabel('Year')
    pyplot.ylabel('Number of Observations')

    pyplot.xticks(years)

    pyplot.show()


def extract_years(observations: [observation.Observation]) -> []:
    return [datetime.datetime.strptime(obs.observed_on, "%Y-%m-%d").year for obs in observations]


def extract_year_observation_counts(observations: [observation.Observation]):
    year_counts = Counter(extract_years(observations))

    years = list(year_counts.keys())
    numbers = list(year_counts.values())

    return [years, numbers]
