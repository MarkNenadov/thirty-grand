from src.thirty_grand.utilities.tables import print_observations_table
from src.thirty_grand import queries
from src.thirty_grand.utilities.csv import read_csv
from thirty_grand.utilities import is_probable_species

data = read_csv("../../data/observations.csv")

all_observations = queries.query_all_observations(data, scientific_name_partial="Pantherophis vulpinus")

print_observations_table(
    all_observations,
    (
        ('Observation ID', 'obs_id'),
        ("Observed On", 'observed_on'),
        ("Time Observed At", 'time_observed_at'),
        ("Scientific Name", 'scientific_name'),
        ("Common Name", 'common_name'),
        ("Place ", 'place_guess')
    )
)
