import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.config import load_settings

def test_load_settings():
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'settings.yml'))
    settings = load_settings(config_path)
    
    assert settings.logo_url.startswith("https://")
    assert isinstance(settings.features.enable_vector_search, bool)
