from src.thirty_grand.utilities.tables import print_family_table
from src.thirty_grand import queries
from src.thirty_grand.utilities.csv import read_csv

data = read_csv("../data/observations.csv")

all_observations = queries.query_all_observations(data)

print("Mark Nenadov's LaSalle Yard Diptera Family Tally")

print_family_table(all_observations, threshold=1, filter_property="order_name", filter_value="Diptera", filter_place_guess="huron church line")
