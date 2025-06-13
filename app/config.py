from pydantic import BaseModel
from typing import Optional
import yaml

class FeatureFlags(BaseModel):
    enable_vector_search: bool = True
    enable_email_draft: bool = False

class Settings(BaseModel):
    logo_url: str
    features: FeatureFlags

def load_settings(path: str = "settings.yaml") -> Settings:
    with open(path, "r") as file:
        config_dict = yaml.safe_load(file)
    return Settings(**config_dict)
