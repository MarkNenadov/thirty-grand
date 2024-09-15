from collections import defaultdict

from prettytable import PrettyTable

from src.thirty_grand import observation
from thirty_grand.utilities.formatting import format_taxon_name


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


def get_property_observation_counts(
        observations, property_name,
        filter_property = None,
        filter_by_value = None,
        filter_place_guess: str = None
) -> dict:
    """
    Count occurrences of property within obervation list (with option to filter) and return as a dictionary

    Parameters:
        observations: The list of observations
        property_name: The property as it appears on the observation object
        filter_property: An additional property to filter on
        filter_by_value: The value expected in filter_property to execute the filter
        filter_place_guess: partial match filter on place guess

    """
    property_counts = defaultdict(int)
    for obs in observations:
        property_value = getattr(obs, property_name, "")
        filter_value = getattr(obs, filter_property, "") if filter_property and filter_by_value else ""

        if property_value != "" and (filter_by_value is None or filter_value == filter_by_value) and (filter_place_guess is None or filter_place_guess == "" or (filter_place_guess.lower() in obs.place_guess.lower())):
            property_counts[property_value] += 1
    return dict(property_counts)


def get_property_distinct_species_count(
        taxon_property_name: str,
        taxon_name: str,
        observations:[observation.Observation],
        filter_place_guess: str = ""
) -> int:
    distinct_species = set()
    for obs in observations:
        if (filter_place_guess is None or filter_place_guess == "" or (filter_place_guess.lower() in obs.place_guess.lower())):
            taxon_property_value = getattr(obs, taxon_property_name, "")
            if _is_probable_species(obs.scientific_name) and taxon_property_value == taxon_name:
                distinct_species.add(obs.scientific_name)

    return len(distinct_species)


def _is_probable_species(scientific_name: str) -> bool:
    split_by_species = scientific_name.split(" ")

    return len(split_by_species) >= 2 and len(split_by_species) < 4

def get_taxon_table_str(observations: [observation.Observation],
                        threshold: int,
                        taxon_property_name: str,
                        filter_property: str = None,
                        filter_value: str = None,
                        filter_place_guess: str = None):
    """
    Get table of observations per given Taxon with a threshold amount.

    Parameters:
        observations: The list of observations
        threshold: Only show classes that have at least this number of observations
        taxon_property_name: Name of which taxon we are working with
        filter_property: The naem of the taxon property to use
        filter_value: The value expected for filter in filter_property
        filter_place_guess: Partial match filter on place guess
    """
    assert taxon_property_name is not None, "get_taxon_table_str requires taxon_property_name"
    assert taxon_property_name.endswith("_name"), "get_taxon_table_str requires taxon_property_name ending with '_name'"

    taxon_observation_counts_dict = get_property_observation_counts(
        observations,
        taxon_property_name,
        filter_property,
        filter_value,
        filter_place_guess
    )
    sorted_taxon_counts = sorted(taxon_observation_counts_dict.items(), key=lambda item: item[1], reverse=True)

    table = PrettyTable()
    table.field_names = [
        "Count",
        format_taxon_name(taxon_property_name),
        "Number of Observations",
        "Distinct Species"
    ]

    count = 0
    for taxon_name, taxon_name_count in sorted_taxon_counts:
        if taxon_name_count >= threshold:
            count += 1
            table.add_row(
                [
                    count,
                    taxon_name,
                    taxon_name_count,
                    get_property_distinct_species_count(taxon_property_name, taxon_name, observations, filter_place_guess)
                ]
            )
    return table.get_string()


def print_observations_table(observations: [observation.Observation]) -> None:
    print(get_observations_table_str(observations))


def print_class_table(observations: [observation.Observation], threshold: int) -> None:
    print(get_taxon_table_str(observations, threshold, "class_name"))


def print_family_table(
        observations: [observation.Observation],
        threshold: int = 1,
        filter_property: str = None,
        filter_value: str = None,
        filter_place_guess: str = None,
) -> None:
    print(get_taxon_table_str(observations, threshold, "family_name", filter_property, filter_value, filter_place_guess))


def print_genera_table(observations: [observation.Observation], threshold: int = 1, filter_property: str = None, filter_value: str = None) -> None:
    print(get_taxon_table_str(observations, threshold, "family_name", filter_property, filter_value))


def print_order_table(
        observations: [observation.Observation],
        threshold: int = 1,
        filter_place_guess: str = ""
) -> None:
    print(get_taxon_table_str(observations, threshold, "order_name", filter_place_guess=filter_place_guess))
