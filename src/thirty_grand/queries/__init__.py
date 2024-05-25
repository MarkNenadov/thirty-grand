from .. import observation


def query_all_observations(data, scientific_name_partial=None):
    observations = []

    for _, row in data.iterrows():
        row_scientific_name = row['scientific_name'] or ""
        has_row_scientific_name = isinstance(row_scientific_name, str) and row_scientific_name != ""

        has_scientific_name_partial = scientific_name_partial is not None

        scientific_name_match = has_scientific_name_partial and has_row_scientific_name and scientific_name_partial.lower() in row_scientific_name.lower()

        if scientific_name_partial is None or scientific_name_match:
            observations.append(observation.Observation.create_from_row(row))
    return observations
