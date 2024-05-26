from .. import observation


def query_all_observations(
        data,
        scientific_name_partial=None,
        common_name_partial=None
) -> [observation.Observation]:
    observations = []

    for _, row in data.iterrows():
        row_common_name = row['common_name'] or ""
        has_row_common_name = isinstance(row_common_name, str) and row_common_name != ""
        has_common_name_partial = common_name_partial is not None
        common_name_match = has_common_name_partial and has_row_common_name and common_name_partial.lower() in row_common_name.lower()

        row_scientific_name = row['scientific_name'] or ""
        has_row_scientific_name = isinstance(row_scientific_name, str) and row_scientific_name != ""
        has_scientific_name_partial = scientific_name_partial is not None
        scientific_name_match = has_scientific_name_partial and has_row_scientific_name and scientific_name_partial.lower() in row_scientific_name.lower()

        if (scientific_name_partial is None or scientific_name_match) and (common_name_partial is None or common_name_match):
            observations.append(observation.Observation.create_from_row(row))
    return observations
