#!/usr/bin/env python3
import os, sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

port = int(os.environ.get('PORT', 8787))
directory = os.path.expanduser('~/Downloads/vesper 19/project')

os.chdir(directory)
server = HTTPServer(('', port), SimpleHTTPRequestHandler)
print(f'Serving {directory} on port {port}', flush=True)
server.serve_forever()
