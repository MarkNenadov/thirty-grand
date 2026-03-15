import datetime
from dataclasses import dataclass, field

import pandas as pd


@dataclass
class Observation:
    """
    Represents an observation of a species from inaturalist csv export.
    """
    obs_id: int
    observed_on_string: str
    observed_on: str
    time_observed_at: str
    class_name: str
    order_name: str
    family_name: str
    scientific_name: str
    common_name: str
    place_guess: str
    iconic_taxon_name: str
    taxon_id: str
    longitude: str = field(repr=False)
    latitude: str = field(repr=False)
    image_url: str = field(repr=False)

    def get_year(self) -> int:
        return datetime.datetime.strptime(self.observed_on, "%Y-%m-%d").year

    @staticmethod
    def create_from_row(row: pd.Series) -> "Observation":
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
