# Playwright Learning Python

A Python Playwright framework using pytest and the Page Object Model.

## Structure

- `pages/` – page objects
- `tests/` – test cases and fixtures
- `utils/` – configuration and server helpers
- `site/` – static demo pages for learning

## Setup

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
pytest -q
```
