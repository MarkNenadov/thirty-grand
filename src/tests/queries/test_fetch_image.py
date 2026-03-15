import base64
from unittest.mock import Mock, patch

import pytest

from thirty_grand.observation import Observation
from thirty_grand.queries import fetch_image


@pytest.fixture
def observation() -> Mock:
    obs = Mock(spec=Observation)
    obs.image_url = "https://inaturalist.org/photos/123/medium.jpg"
    return obs


def test_fetch_image_replaces_medium_with_large_in_url(observation) -> None:
    mock_response = Mock()
    mock_response.content = b"fake image content"

    with patch("thirty_grand.queries.requests.get", return_value=mock_response) as mock_get:
        fetch_image(observation)
        mock_get.assert_called_once_with("https://inaturalist.org/photos/123/large.jpg")


def test_fetch_image_returns_base64_encoded_content(observation) -> None:
    mock_response = Mock()
    mock_response.content = b"fake image content"

    with patch("thirty_grand.queries.requests.get", return_value=mock_response):
        result = fetch_image(observation)

    assert result == base64.b64encode(b"fake image content")
