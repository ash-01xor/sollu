import os
import shutil
from pathlib import Path
from dotenv import load_dotenv , set_key
from google.genai import Client

CONFIG_DIR = Path.home() / ".config" / "sollu"
ENV_FILE = CONFIG_DIR / ".env"
MODEL_NAME = "gemini-2.0-flash"

def get_api_key():
    if ENV_FILE.exists():
        load_dotenv(ENV_FILE)
    api_key = os.environ.get("GEMINI_API_KEY")
    return api_key

def save_api_key(api_key):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    set_key(ENV_FILE, "GEMINI_API_KEY", api_key)

def delete_api_key():
    if ENV_FILE.exists():
        ENV_FILE.unlink() 
        return True
    return False

def delete_all_config():
    if CONFIG_DIR.exists():
        shutil.rmtree(CONFIG_DIR) 
        return True
    return False

def configure_gemini_client():

    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key must be provided or set in the environment.")

    client = Client(api_key=api_key)
    return client

