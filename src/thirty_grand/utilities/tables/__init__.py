"""
Table generation utilities for wildlife observations.

This module provides functions for creating formatted tables of wildlife observation data,
including taxonomic summaries and observation details.
"""

from collections import defaultdict
from typing import Dict, List, Optional

from prettytable import PrettyTable

from thirty_grand.observation import Observation
from thirty_grand.queries import _name_matches
from thirty_grand.utilities import is_probable_species
from thirty_grand.utilities.formatting import format_taxon_name


def get_observations_table_str(
        observations: List[Observation],
        display_configuration: tuple[tuple[str, str], ...] = (
            ('Observation ID', 'obs_id'),
            ("Observed On", 'observed_on'),
            ("Time Observed At", 'time_observed_at'),
            ("Scientific Name", 'scientific_name'),
            ("Common Name", 'common_name'),
            ("Iconic Taxon Name", 'iconic_taxon_name')
        )
) -> str:
    """
    Generate a formatted table string of observations.
    
    Args:
        observations: List of Observation objects to display
        display_configuration: Tuple of (display_name, attribute_name) pairs
        
    Returns:
        str: Formatted table string
        
    Raises:
        ValueError: If observations list is empty or display_configuration is invalid
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
    if not display_configuration:
        raise ValueError("Display configuration cannot be empty")
        
    table = PrettyTable()
    table.field_names = [item[0] for item in display_configuration]
    
    for obs in observations:
        table.add_row([getattr(obs, item[1], '') for item in display_configuration])
        
    return table.get_string()


def get_property_observation_counts(
    observations: List[Observation],
    property_name: str,
    filter_property: Optional[str] = None,
    filter_by_value: Optional[str] = None,
    filter_place_guess: Optional[str] = None
) -> Dict[str, int]:
    """
    Count occurrences of a property within observations with optional filtering.
    
    Args:
        observations: List of Observation objects to analyze
        property_name: Name of the property to count
        filter_property: Optional property name to filter on
        filter_by_value: Optional value to filter by
        filter_place_guess: Optional place name to filter by
        
    Returns:
        Dict[str, int]: Dictionary mapping property values to their counts
        
    Raises:
        ValueError: If observations list is empty or property_name is invalid
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
    if not property_name:
        raise ValueError("Property name cannot be empty")
        
    property_counts = defaultdict(int)
    
    for obs in observations:
        property_value = getattr(obs, property_name, "")
        filter_value = getattr(obs, filter_property, "") if filter_property and filter_by_value else ""
        
        if (
            property_value and
            (filter_by_value is None or filter_value == filter_by_value) and
            (filter_place_guess is None or not filter_place_guess or
             filter_place_guess.lower() in obs.place_guess.lower())
        ):
            property_counts[property_value] += 1
            
    return dict(property_counts)


def get_property_distinct_species_count(
    taxon_property_name: str,
    taxon_name: str,
    observations: List[Observation],
    filter_place_guess: str = ""
) -> int:
    """
    Count distinct species within a taxon group.
    
    Args:
        taxon_property_name: Name of the taxon property to filter on
        taxon_name: Value of the taxon to count species for
        observations: List of Observation objects to analyze
        filter_place_guess: Optional place name to filter by
        
    Returns:
        int: Number of distinct species
        
    Raises:
        ValueError: If observations list is empty
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
        
    distinct_species = set()
    
    for obs in observations:
        if (
            not filter_place_guess or
            filter_place_guess.lower() in obs.place_guess.lower()
        ):
            taxon_property_value = getattr(obs, taxon_property_name, "")
            if is_probable_species(obs.scientific_name) and taxon_property_value == taxon_name:
                distinct_species.add(obs.scientific_name)
                
    return len(distinct_species)


def get_taxon_table_str(
    observations: List[Observation],
    threshold: int,
    taxon_property_name: str,
    filter_property: Optional[str] = None,
    filter_value: Optional[str] = None,
    filter_place_guess: Optional[str] = None
) -> str:
    """
    Generate a formatted table of taxon observations.
    
    Args:
        observations: List of Observation objects to analyze
        threshold: Minimum number of observations to include
        taxon_property_name: Name of the taxon property to analyze
        filter_property: Optional property name to filter on
        filter_value: Optional value to filter by
        filter_place_guess: Optional place name to filter by
        
    Returns:
        str: Formatted table string
        
    Raises:
        ValueError: If observations list is empty or taxon_property_name is invalid
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
    if not taxon_property_name:
        raise ValueError("Taxon property name cannot be empty")
    if not taxon_property_name.endswith("_name"):
        raise ValueError("Taxon property name must end with '_name'")
        
    taxon_counts = get_property_observation_counts(
        observations,
        taxon_property_name,
        filter_property,
        filter_value,
        filter_place_guess
    )
    
    sorted_taxon_counts = sorted(
        taxon_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )
    
    table = PrettyTable()
    table.field_names = [
        "Count",
        format_taxon_name(taxon_property_name),
        "Number of Observations",
        "Distinct Species"
    ]
    
    count = 0
    for taxon_name, taxon_count in sorted_taxon_counts:
        if taxon_count >= threshold:
            count += 1
            table.add_row([
                count,
                taxon_name,
                taxon_count,
                get_property_distinct_species_count(
                    taxon_property_name,
                    taxon_name,
                    observations,
                    filter_place_guess
                )
            ])
            
    return table.get_string()


def print_observations_table(
    observations: List[Observation],
    display_configuration: tuple[tuple[str, str], ...] = (
        ('Observation ID', 'obs_id'),
        ("Observed On", 'observed_on'),
        ("Time Observed At", 'time_observed_at'),
        ("Scientific Name", 'scientific_name'),
        ("Common Name", 'common_name'),
        ("Iconic Taxon Name", 'iconic_taxon_name')
    )
) -> None:
    """
    Print a formatted table of observations.
    
    Args:
        observations: List of Observation objects to display
        display_configuration: tuple of (display_name, attribute_name) pairs
    """
    print(get_observations_table_str(observations, display_configuration))


def print_class_table(observations: List[Observation], threshold: int) -> None:
    """
    Print a formatted table of class-level observations.
    
    Args:
        observations: List of Observation objects to analyze
        threshold: Minimum number of observations to include
    """
    print(get_taxon_table_str(observations, threshold, "class_name"))


def print_family_table(
    observations: List[Observation],
    threshold: int = 1,
    filter_property: Optional[str] = None,
    filter_value: Optional[str] = None,
    filter_place_guess: Optional[str] = None
) -> None:
    """
    Print a formatted table of family-level observations.
    
    Args:
        observations: List of Observation objects to analyze
        threshold: Minimum number of observations to include
        filter_property: Optional property name to filter on
        filter_value: Optional value to filter by
        filter_place_guess: Optional place name to filter by
    """
    print(get_taxon_table_str(
        observations,
        threshold,
        "family_name",
        filter_property,
        filter_value,
        filter_place_guess
    ))


def print_genera_table(
    observations: List[Observation],
    threshold: int = 1,
    filter_property: Optional[str] = None,
    filter_value: Optional[str] = None
) -> None:
    """
    Print a formatted table of genus-level observations.
    
    Args:
        observations: List of Observation objects to analyze
        threshold: Minimum number of observations to include
        filter_property: Optional property name to filter on
        filter_value: Optional value to filter by
    """
    print(get_taxon_table_str(
        observations,
        threshold,
        "genus_name",
        filter_property,
        filter_value
    ))


def print_order_table(
    observations: List[Observation],
    threshold: int = 1,
    filter_place_guess: str = ""
) -> None:
    """
    Print a formatted table of order-level observations.
    
    Args:
        observations: List of Observation objects to analyze
        threshold: Minimum number of observations to include
        filter_place_guess: Optional place name to filter by
    """
    print(get_taxon_table_str(
        observations,
        threshold,
        "order_name",
        filter_place_guess=filter_place_guess
    ))


def _get_distinct_species_to_common_names(observations: [Observation], taxon_property_name: str, filter_value: str) -> dict:
    assert len(observations) > 0
    species_to_common_name = {}
    for obs in observations:
        if _name_matches(filter_value, getattr(obs, taxon_property_name, "")):
            if is_probable_species(obs.scientific_name):
                species_to_common_name[obs.scientific_name] = obs.common_name

    return species_to_common_name


def print_distinct_species_in_taxon(observations: [Observation], taxon_property_name: str, filter_value: str) -> None:
    assert len(observations) > 0
    species_to_common_name = _get_distinct_species_to_common_names(observations, taxon_property_name, filter_value)
    table = PrettyTable()
    table.field_names = [
        "Count",
        "Species",
        "Common Name"
    ]

    count = 0
    for species, common_name in dict(sorted(species_to_common_name.items())).items():
        count += 1
        table.add_row(
            [
                count,
                species,
                common_name,
            ]
        )
    print(table.get_string())
