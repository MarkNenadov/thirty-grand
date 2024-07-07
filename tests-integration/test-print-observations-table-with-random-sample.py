import pandas as pd

from src.thirty_grand.queries import random_sample
from src.thirty_grand.utilities.tables import print_observations_table

data = pd.read_csv("../data/observations.csv", low_memory=False)

print_observations_table(random_sample(data,5))
