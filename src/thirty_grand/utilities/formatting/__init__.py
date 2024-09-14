def format_taxon_name(taxon_property_name: str) -> str:
    """
    Take in, for instance, class_name and return Class

    :param taxon_property_name:
    :return: str

    """
    return taxon_property_name.split("_")[0].capitalize()

