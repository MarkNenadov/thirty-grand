import pytest
from thirty_grand.utilities.formatting import format_taxon_name


def test_format_taxon_name():
    assert format_taxon_name("class_name") == "Class"
    assert format_taxon_name("order_name") == "Order"
    assert format_taxon_name("order") == "Order"

if __name__ == '__main__':
    pytest.main()
