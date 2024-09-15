from src.thirty_grand import queries
from src.thirty_grand.utilities.csv import read_csv
from thirty_grand.utilities.tables import print_distinct_species_in_taxon

data = read_csv("../../data/observations.csv")

all_observations = queries.query_all_observations(data)

print_distinct_species_in_taxon(all_observations, "class_name", "Reptilia")
