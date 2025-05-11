from unittest.mock import patch, MagicMock
from sollu.core import get_word_definition , is_valid_word
from google.genai import errors

@patch('sollu.core.configure_gemini_client')
def test_api_error(mock_configure_client):
    """Test handling of API errors."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = errors.APIError(
        code="500", response_json={"message": "Internal Server Error"}
    )
    mock_client = MagicMock()
    mock_client.models = mock_model
    mock_configure_client.return_value = mock_client

    result = get_word_definition("test")
    assert result["error"] == "API Error"

@patch('sollu.core.configure_gemini_client')
def test_general_exception(mock_configure_client):
    """Test handling of general exceptions."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("Unexpected error")
    
    mock_client = MagicMock()
    mock_client.models = mock_model
    mock_configure_client.return_value = mock_client

    result = get_word_definition("test")
    assert "Unexpected Error" in result["error"]

@patch('sollu.core.configure_gemini_client')
def test_invalid_json_response(mock_configure_client):
    """Test handling of invalid JSON in API response."""
    mock_model = MagicMock()
    mock_response = MagicMock()
    mock_response.text = "This is not valid JSON"
    mock_model.generate_content.return_value = mock_response

    mock_client = MagicMock()
    mock_client.models = mock_model
    mock_configure_client.return_value = mock_client

    result = get_word_definition("test")

    assert result["error"] == "Parse Error"
    assert "Failed to parse" in result["details"]


@patch('sollu.core.configure_gemini_client')
def test_empty_response(mock_configure_client):
    """Test handling of empty API response (None returned)."""
    mock_model = MagicMock()
    mock_model.generate_content.return_value = None

    mock_client = MagicMock()
    mock_client.models = mock_model
    mock_configure_client.return_value = mock_client

    result = get_word_definition("test")

    assert "error" in result
    assert result["error"] == "Unexpected Error"
    assert "details" in result

def test_invalid_word_input():
    """Test handling of invalid word inputs (numbers or special characters)."""
    assert not is_valid_word("123")
    assert not is_valid_word("word!")
    assert not is_valid_word("word123")
    assert is_valid_word("hello")
    assert is_valid_word("world")
    assert is_valid_word("well-being")
