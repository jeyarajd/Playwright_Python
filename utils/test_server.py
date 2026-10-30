import os
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from utils.config import SITE_DIR, BASE_URL


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def start_server() -> ThreadingHTTPServer:
    handler = partial(QuietHandler, directory=str(SITE_DIR))
    server = ThreadingHTTPServer(("127.0.0.1", 3001), handler)
    server.daemon_threads = True
    return server


def stop_server(server: ThreadingHTTPServer | None) -> None:
    if server is not None:
        server.shutdown()
        server.server_close()
