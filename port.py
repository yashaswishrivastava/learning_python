# Import the necessary module
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Define server address and port
host = 'localhost'
port = 8000

# Create a handler
handler = SimpleHTTPRequestHandler

# Create the server
server = HTTPServer((host, port), handler)

print(f"Server started at http://{host}:{port}")

# Run the server forever
server.serve_forever()

