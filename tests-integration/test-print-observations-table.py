import pandas as pd

from src.thirty_grand.utilities.tables import print_observations_table
from src.thirty_grand import queries

data = pd.read_csv("../data/observations.csv", low_memory=False)

all_observations = queries.query_all_observations(data)
filtered_observations = [obs for obs in all_observations if " " in obs.scientific_name]

print_observations_table(filtered_observations)
