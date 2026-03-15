"""
Data processing utilities for wildlife observations.

This module provides functions for processing and analyzing wildlife observation data,
including taxonomic classification and temporal analysis.
"""

from collections import Counter

from thirty_grand.observation import Observation


def is_probable_species(scientific_name: str) -> bool:
    """
    Determine if a scientific name likely represents a species-level classification.
    
    A species-level classification typically has 2-3 parts (genus, species, and
    sometimes subspecies).
    
    Args:
        scientific_name: The scientific name to check
        
    Returns:
        bool: True if the name likely represents a species, False otherwise
    """
    if not scientific_name:
        return False
    parts = scientific_name.split()
    return 2 <= len(parts) < 4


def extract_years(observations: list[Observation]) -> list[int]:
    """
    Extract years from a list of observations.
    
    Args:
        observations: List of Observation objects
        
    Returns:
        List[int]: List of years from valid observations
        
    Raises:
        ValueError: If the observations list is empty
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
    return [obs.get_year() for obs in observations if obs.observed_on]


def extract_yearly_observation_counts(observations: list[Observation]) -> tuple[list[int], list[int]]:
    """
    Calculate yearly observation counts from a list of observations.
    
    Args:
        observations: List of Observation objects
        
    Returns:
        Tuple[List[int], List[int]]: A tuple containing:
            - List of years
            - List of observation counts for each year
            
    Raises:
        ValueError: If the observations list is empty
    """
    if not observations:
        raise ValueError("Observations list cannot be empty")
        
    year_counts = Counter(extract_years(observations))
    years, counts = zip(*sorted(year_counts.items()))
    
    return list(years), list(counts) 