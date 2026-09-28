from http.server import BaseHTTPRequestHandler, HTTPServer
import os

VERSION = os.environ.get("VERSION", "dev")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"hello from testrepo {VERSION}\n".encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
