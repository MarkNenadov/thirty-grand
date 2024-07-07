import pandas as pd

from src.thirty_grand.utilities.charting import display_yearly_observation_barchart
from src.thirty_grand import queries

data = pd.read_csv("../data/observations.csv", low_memory=False)

all_observations = queries.query_all_observations(data)
filtered_observations = [obs for obs in all_observations if " " in obs.scientific_name]

display_yearly_observation_barchart(filtered_observations)
