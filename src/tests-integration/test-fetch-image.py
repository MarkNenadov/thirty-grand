import base64

from thirty_grand import queries
from thirty_grand.utilities.csv import read_csv

data = read_csv("../../data/observations.csv")

all_observations = queries.query_all_observations(data, scientific_name_partial="Pantherophis vulpinus")

image_base64 = queries.fetch_image(all_observations[0])
print(image_base64)
