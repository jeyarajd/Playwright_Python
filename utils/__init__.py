import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SITE_DIR = BASE_DIR / "site"


def get_base_url() -> str:
    return "http://localhost:3001"
