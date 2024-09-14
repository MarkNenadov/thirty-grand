import pytest

from thirty_grand.queries import _name_matches


def test__name_matches():
    assert _name_matches("Thamnophis sir", "Thamnophis") == False
    assert _name_matches("Thamnophis sir", "Thamnophis sirtalis") == True
    assert _name_matches("thamnophis sir", "Thamnophis sirtalis") == True
    assert _name_matches(None, "Thamnophis sirtalis") == True

if __name__ == '__main__':
    pytest.main()
