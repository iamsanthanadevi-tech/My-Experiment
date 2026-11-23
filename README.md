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

# PROGRAM:PROGRAM:
from http.server import HTTPServer, SimpleHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)

print("TCP/IP Web Server Started!")
print(f"Open your browser: http://{HOST}:{PORT}")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped.")
    server.server_close()
HTML PROGRAM:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TCP/IP Protocol Suite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

<header>
    <h1>TCP/IP PROTOCOL SUITE</h1>
    <p>Understanding the Language of the Internet</p>
</header>

<nav>
    <a href="#home">Home</a>
    <a href="#about">About</a>
    <a href="#protocols">Protocols</a>
    <a href="#student">Student Details</a>
</nav>

<section id="home" class="hero">
    <h2>Welcome to the World of Networking</h2>
    <p>Explore how devices communicate across the Internet.</p>
</section>

<section id="about" class="about">
    <h2>What is TCP/IP?</h2>
    <p>
        TCP/IP stands for Transmission Control Protocol and
        Internet Protocol. It is a set of communication
        protocols used to connect devices and transfer data.
    </p>
</section>

<section id="protocols">
    <h2 class="section-title">TCP/IP Protocols</h2>
    <div class="protocol-container">

        <div class="protocol-card">
            <h3>TCP</h3>
            <p>Ensures reliable delivery of data.</p>
        </div>

        <div class="protocol-card">
            <h3>IP</h3>
            <p>Handles addressing and routing.</p>
        </div>

        <div class="protocol-card">
            <h3>HTTP</h3>
            <p>Transfers web pages.</p>
        </div>

        <div class="protocol-card">
            <h3>HTTPS</h3>
            <p>Provides secure web communication.</p>
        </div>

        <div class="protocol-card">
            <h3>FTP</h3>
            <p>Transfers files between computers.</p>
        </div>

        <div class="protocol-card">
            <h3>DNS</h3>
            <p>Converts domain names into IP addresses.</p>
        </div>

        <div class="protocol-card">
            <h3>DHCP</h3>
            <p>Assigns IP addresses automatically.</p>
        </div>

        <div class="protocol-card">
            <h3>SMTP</h3>
            <p>Used for sending emails.</p>
        </div>

        <div class="protocol-card">
            <h3>POP3</h3>
            <p>Retrieves emails from a server.</p>
        </div>

        <div class="protocol-card">
            <h3>IMAP</h3>
            <p>Manages emails on a server.</p>
        </div>

    </div>
</section>

<section id="student" class="student">
    <h2>Student Details</h2>
    <p><strong>Name:</strong> Santhanadevi S</p>
    <p><strong>Register Number:</strong> 26018176</p>
    <p><strong>Department:</strong> Computer Science and Engineering</p>
</section>

<footer>
    <p>TCP/IP Protocol Suite | Simple Webserver Experiment</p>
    <p>Designed by Santhanadevi S</p>
</footer>

</body>
</html>
CSS PROGRAM:
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    scroll-behavior: smooth;
}

body {
    font-family: Arial, sans-serif;
    background: #eef2ff;
    color: #202b45;
    line-height: 1.6;
}

header {
    background: linear-gradient(135deg, #101b46, #344c9c, #6878d5);
    color: white;
    text-align: center;
    padding: 55px 20px;
}

header h1 {
    font-size: 38px;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

header p {
    font-size: 17px;
    color: #dce5ff;
}

nav {
    background: #172554;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 35px;
    padding: 17px;
}

nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
    transition: 0.3s;
}

nav a:hover {
    color: #93c5fd;
}

.hero {
    text-align: center;
    padding: 65px 20px;
    background: linear-gradient(120deg, #dbeafe, #ede9fe);
}

.hero h2 {
    font-size: 30px;
    color: #1e3a8a;
    margin-bottom: 15px;
}

.hero p {
    font-size: 17px;
    max-width: 700px;
    margin: auto;
}

.about {
    background: white;
    margin: 35px auto;
    padding: 35px;
    width: 85%;
    border-radius: 15px;
    box-shadow: 0 5px 18px rgba(30, 58, 138, 0.10);
    text-align: center;
}

.about h2 {
    color: #344c9c;
    margin-bottom: 15px;
}

.section-title {
    text-align: center;
    color: #1e3a8a;
    font-size: 29px;
    margin: 45px 0 25px;
}

.protocol-container {
    width: 88%;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 22px;
    padding-bottom: 40px;
}

.protocol-card {
    background: white;
    padding: 27px 22px;
    border-radius: 14px;
    border-top: 5px solid #536dce;
    box-shadow: 0 5px 15px rgba(30, 58, 138, 0.10);
    transition: transform 0.3s, box-shadow 0.3s;
    text-align: center;
}

.protocol-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 10px 22px rgba(30, 58, 138, 0.18);
}

.protocol-card h3 {
    color: #344c9c;
    font-size: 23px;
    margin-bottom: 10px;
}

.student {
    background: linear-gradient(135deg, #1e3a8a, #536dce);
    color: white;
    width: 85%;
    margin: 20px auto 45px;
    padding: 35px;
    border-radius: 15px;
    text-align: center;
}

.student h2 {
    margin-bottom: 15px;
}

footer {
    background: #101b46;
    color: white;
    text-align: center;
    padding: 22px;
}

@media (max-width: 600px) {
    header h1 {
        font-size: 27px;
    }

    nav {
        gap: 18px;
    }

    .about, .student {
        width: 92%;
    }
}

# OUTPUT:![TCP AND IP](<TCP AND IP.png>)
# RESULT:
Thus, the simple web server was successfully developed and executed in localhost (127.0.0.1:8000) to serve HTML pages and display the TCP/IP Protocol Suite protocols.
