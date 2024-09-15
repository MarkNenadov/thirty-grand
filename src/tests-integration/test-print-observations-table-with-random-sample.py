from src.thirty_grand.queries import random_sample
from src.thirty_grand.utilities.tables import print_observations_table
from src.thirty_grand.utilities.csv import read_csv

data = read_csv("../../data/observations.csv")

print_observations_table(random_sample(data,5))
