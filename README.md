# EX01 Developing a Simple Webserver

# Date:15-11-2026
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:from http.server import HTTPServer, SimpleHTTPRequestHandler

server_address = ("127.0.0.1", 8000)

http_server = HTTPServer(
    server_address,
    SimpleHTTPRequestHandler
)

print("Web Server is running...")
print("Open http://127.0.0.1:8000")

http_server.serve_forever()
# OUTPUT:<img width="1920" height="1080" alt="output" src="https://github.com/user-attachments/assets/38652850-9db1-4acf-afca-03f31d4b5b3a" />

# RESULT:
Thus, the simple web server was successfully developed and executed in localhost (127.0.0.1:8000) to serve HTML pages and display the TCP/IP Protocol Suite protocols.
