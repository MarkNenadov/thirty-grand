import pytest
from thirty_grand.utilities.tables import is_probable_species


def test_is_probable_species():
    assert is_probable_species("Diptera") == False
    assert is_probable_species("Thomnophis sirtalis sirtalis") == True
    assert is_probable_species("Actias luna") == True
    assert is_probable_species("Actias luna luna luna") == False

if __name__ == '__main__':
    pytest.main()
