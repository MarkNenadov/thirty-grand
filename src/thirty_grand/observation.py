from dataclasses import dataclass

import pandas as pd


@dataclass
class Observation:
    """
    Represents an observation of a species from inaturalist csv export.
    """
    def __init__(
            self,
            obs_id,
            observed_on_string,
            observed_on,
            time_observed_at,
            class_name,
            family_name,
            scientific_name,
            common_name,
            iconic_taxon_name,
            taxon_id
    ):
        self.obs_id = obs_id
        self.observed_on_string = observed_on_string
        self.observed_on = observed_on
        self.time_observed_at = time_observed_at
        self.family_name = family_name
        self.class_name = class_name
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.iconic_taxon_name = iconic_taxon_name
        self.taxon_id = taxon_id
        
    def __repr__(self) -> str:
        return (f"Observation(obs_id={self.obs_id}, "
                f"observed_on_string='{self.observed_on_string}', "
                f"observed_on='{self.observed_on}', "
                f"time_observed_at='{self.time_observed_at}', "
                f"family_name='{self.family_name}', "
                f"class_name='{self.class_name}', "
                f"scientific_name='{self.scientific_name}', "
                f"common_name='{self.common_name}', "
                f"iconic_taxon_name='{self.iconic_taxon_name}', "
                f"taxon_id={self.taxon_id})")

    @staticmethod
    def create_from_row(row: dict):
        return Observation(
            obs_id=row['id'],
            observed_on_string=row['observed_on_string'],
            observed_on='' if pd.isna(row['observed_on']) else row['observed_on'],
            time_observed_at=row['time_observed_at'],
            class_name=row['taxon_class_name'],
            family_name=row['taxon_family_name'],
            scientific_name='' if pd.isna(row['scientific_name']) else row['scientific_name'],
            common_name=row['common_name'],
            iconic_taxon_name=row['iconic_taxon_name'],
            taxon_id=row['taxon_id']
        )
