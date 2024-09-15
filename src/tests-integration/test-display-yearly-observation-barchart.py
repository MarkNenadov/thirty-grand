from src.thirty_grand.utilities.charting import display_yearly_observation_barchart
from src.thirty_grand import queries
from src.thirty_grand.utilities.csv import read_csv

data = read_csv("../../data/observations.csv")

all_observations = queries.query_all_observations(data)

display_yearly_observation_barchart(all_observations)
