import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


def load_json(name: str):
    path = DATA_DIR / name
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
