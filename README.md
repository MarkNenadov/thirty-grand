# thirty-grand

## Introduction

Some tools for exploring and visualizing my 30,000 observations of animals and plants on iNaturalist. Utilizing Python, pandas, and matplotlib.

You can see a (work in progress) report on these 30,000 observation with many photos [here](https://docs.google.com/document/d/19-Nd1FMf-i1crleeBk0qfocPLEZFZPEB0-CNjl1a2Ac/edit?usp=sharing).

Mark Nenadov (2024)

## Module Structure

### Queries
- query_all_observations (function)
- random_sample (function)

### Utilities

Charting
- display_yearly_observation_barchart (function using matplotlib)

Tables
- get_observations_table_str (function)
- print_observations_table (function)
- get_taxon_table_str (function)
- print_family_table (function)
- print_class_table (function)
- print_genera_table (function)
- print_order_table (function)
- print_distinct_species_in_taxon (function)

