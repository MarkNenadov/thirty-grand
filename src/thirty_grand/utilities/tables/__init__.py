from prettytable import PrettyTable

from src.thirty_grand import observation


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
