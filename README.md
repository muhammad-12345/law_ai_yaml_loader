# YAML Loader Showcase

This is a minimal FastAPI app to demonstrate a YAML-based configuration system using Pydantic and PyYAML.

## Features
- Load settings from `settings.yaml`
- Validate using Pydantic models
- Expose loaded settings via API

## Run the App

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
