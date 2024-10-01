def format_taxon_name(taxon_property_name: str) -> str:
    """
    Take in, for instance, class_name and return Class

    :param taxon_property_name:
    :return: str

    """
    assert taxon_property_name is not None
    assert taxon_property_name != ""

    return taxon_property_name.split("_")[0].capitalize()

