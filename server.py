
from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ("127.0.0.1", 8000)

http_server = HTTPServer(
    server_address,
    SimpleHTTPRequestHandler
)

print("Web Server is running...")
print("Open http://127.0.0.1:8000")

http_server.serve_forever()
