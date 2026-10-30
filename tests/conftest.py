import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import threading

import pytest
from playwright.sync_api import Browser, Page, sync_playwright

from utils.test_server import start_server, stop_server


@pytest.fixture(scope="session")
def web_server():
    server = start_server()
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield server
    stop_server(server)
    thread.join(timeout=2)


@pytest.fixture
def page(web_server):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
