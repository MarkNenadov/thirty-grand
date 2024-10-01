import datetime
from dataclasses import dataclass

import pandas as pd
from pandas.core import series


@dataclass
class Observation:
    """
    Represents an observation of a species from inaturalist csv export.
    """
    def __init__(
            self,
            obs_id,
            observed_on_string: str,
            observed_on: str,
            time_observed_at: str,
            class_name: str,
            order_name: str,
            family_name: str,
            scientific_name: str,
            common_name: str,
            place_guess: str,
            iconic_taxon_name: str,
            taxon_id: str,
            longitude: str,
            latitude: str,
            image_url: str,
    ) -> None:
        self.obs_id = obs_id
        self.observed_on_string = observed_on_string
        self.observed_on = observed_on
        self.time_observed_at = time_observed_at
        self.class_name = class_name
        self.order_name = order_name
        self.family_name = family_name
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.place_guess = place_guess
        self.iconic_taxon_name = iconic_taxon_name
        self.taxon_id = taxon_id
        self.longitude = longitude
        self.latitude = latitude
        self.image_url = image_url

    def __repr__(self) -> str:
        return (f"Observation(obs_id={self.obs_id}, "
                f"observed_on_string='{self.observed_on_string}', "
                f"observed_on='{self.observed_on}', "
                f"time_observed_at='{self.time_observed_at}', "
                f"class_name='{self.class_name}', "
                f"order_name='{self.order_name}', "
                f"family_name='{self.family_name}', "
                f"scientific_name='{self.scientific_name}', "
                f"common_name='{self.common_name}', "
                f"place_guess='{self.place_guess}', "
                f"iconic_taxon_name='{self.iconic_taxon_name}', "
                f"taxon_id={self.taxon_id})")

    def get_year(self) -> int:
        return datetime.datetime.strptime(self.observed_on, "%Y-%m-%d").year

    @staticmethod
    def create_from_row(row: series) -> object:
        assert row is not None
        return Observation(
            obs_id=row['id'],
            observed_on_string=row['observed_on_string'],
            observed_on='' if pd.isna(row['observed_on']) else row['observed_on'],
            time_observed_at=row['time_observed_at'],
            class_name=row['taxon_class_name'],
            order_name=row['taxon_order_name'],
            family_name=row['taxon_family_name'],
            scientific_name='' if pd.isna(row['scientific_name']) else row['scientific_name'],
            common_name=row['common_name'],
            place_guess=row['place_guess'],
            iconic_taxon_name=row['iconic_taxon_name'],
            taxon_id=row['taxon_id'],
            longitude=row['longitude'],
            latitude=row['latitude'],
            image_url=row['image_url'],
        )
