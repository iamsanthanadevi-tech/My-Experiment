
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("TCP/IP Web Server Started!")
print(f"Open your browser: http://{HOST}:{PORT}")

server.serve_forever()
