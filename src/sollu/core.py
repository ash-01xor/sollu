import re
import json
from typing import Dict, Any
from google.genai import errors
from .configs.config import configure_gemini_client, MODEL_NAME
from .configs.prompt import DEFINITION_PROMPT
from .schema import ErrorResponse

def is_valid_word(word):
    """Check if the input is a valid word.

    Args:
        word (str): The input word to be checked.

    Returns:
        bool: True if the word is valid (contains only letters), False otherwise.
    """
    return bool(re.match(r'^[a-zA-Z]+(-[a-zA-Z]+)*$', word))

def get_word_definition(word: str) -> Dict[str, Any]:
    """
    Get the definition and example sentence for a word using Gemini API.
    
    Args:
        word: The word to look up
        
    Returns:
        Dictionary containing word, definition, and example
        
    Raises:
        ValueError: If there's an issue with the API or response
    """
    try:
        client = configure_gemini_client()
        prompt = DEFINITION_PROMPT.format(word=word)
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
            },
        )
            
        try:
            result = json.loads(response.text)
            return result
        
        except json.JSONDecodeError as e:
            return ErrorResponse(
                error="Parse Error",
                details=f"Failed to parse API response: {str(e)}"
            ).model_dump()
            
    except errors.APIError as e:
        return ErrorResponse(
            error="API Error",
            details=f"Code: {e.code}, Message: {e.message}"
        ).model_dump()
        
    except Exception as e:
        return ErrorResponse(
            error="Unexpected Error",
            details=str(e)
        ).model_dump()