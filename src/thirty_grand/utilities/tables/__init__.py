from collections import defaultdict

from prettytable import PrettyTable

from src.thirty_grand import observation


def get_observations_table_str(observations: [observation.Observation]) -> str:
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


def get_property_counts(observations, property_name, filter_property = None, filter_by_value = None) -> dict:
    """
    Count occurrences of property within obervation list (with option to filter) and return as a dictionary

    Parameters:
        observations: The list of observations
        property_name: The property as it appears on the observation object
        filter_property: An additional property to filter on
        filter_by_value: The value expected in filter_property to execute the filter

    """
    property_counts = defaultdict(int)
    for obs in observations:
        property_value = getattr(obs, property_name, "")
        filter_value = getattr(obs, filter_property, "") if filter_property and filter_by_value else ""

        if property_value != "" and (filter_by_value is None or filter_value == filter_by_value):
            property_counts[property_value] += 1
    return dict(property_counts)


def get_taxon_table_str(observations: [observation.Observation],
                        threshold: int,
                        taxon_property_name: str,
                        filter_property: str = None,
                        filter_value: str = None):
    """
    Get table of observations per given Taxon with a threshold amount.

    Parameters:
        observations: The list of observations
        threshold: Only show classes that have at least this number of observations
        filter_property: The naem of the taxon property to use
        filter_value: The value expected for filter in filter_property
    """
    assert taxon_property_name is not None, "get_taxon_table_str requires taxon_property_name"
    assert taxon_property_name.endswith("_name"), "get_taxon_table_str requires taxon_property_name ending with '_name'"

    taxon_counts_dict = get_property_counts(observations, taxon_property_name, filter_property, filter_value)
    sorted_taxon_counts = sorted(taxon_counts_dict.items(), key=lambda item: item[1], reverse=True)


    table = PrettyTable()
    table.field_names = [
        taxon_property_name.split("_")[0].capitalize(),
        "Number of Observations",
    ]

    for taxon_name, taxon_name_count in sorted_taxon_counts:
        if taxon_name_count >= threshold:
            table.add_row(
                [
                    taxon_name,
                    taxon_name_count,
                ]
            )
    return table.get_string()


def print_observations_table(observations: [observation.Observation]) -> None:
    print(get_observations_table_str(observations))


def print_class_table(observations: [observation.Observation], threshold: int) -> None:
    print(get_taxon_table_str(observations, threshold, "class_name"))


def print_family_table(observations: [observation.Observation], threshold: int = 1, filter_property: str = None, filter_value: str = None) -> None:
    print(get_taxon_table_str(observations, threshold, "family_name", filter_property, filter_value))


def print_order_table(observations: [observation.Observation], threshold: int = 1) -> None:
    print(get_taxon_table_str(observations, threshold, "order_name"))
