from typing import List

import matplotlib.pyplot as pyplot

from src.thirty_grand.utilities import extract_yearly_observation_counts
from thirty_grand.observation import Observation


def display_yearly_observation_barchart(observations: List[Observation],
                                        figure_size:tuple[float, float]=(13,7)) -> None:
    """
    Display a bar chart of iNaturalist observation counts per year.

    Parameters:
        observations: A list of observations from inaturalist csv export.
        figure_size: Size of the chart, x, y
    """
    assert len(observations) > 0
    years, numbers = extract_yearly_observation_counts(observations)

    pyplot.figure(figsize=figure_size)
    pyplot.bar(years, numbers, color='skyblue')

    pyplot.title('Number of Observations Per Year')
    pyplot.xlabel('Year')
    pyplot.ylabel('Number of Observations')

    pyplot.xticks(years)
    pyplot.tight_layout()

    pyplot.show()
