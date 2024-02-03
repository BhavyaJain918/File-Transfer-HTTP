import socket
import subprocess
import sys
from http.server import HTTPServer , BaseHTTPRequestHandler
host = socket.gethostbyname(socket.gethostname())
port = 8000
global server1
try:
    args = f"python -m http.server {port} -b {host}"
    command = input("Enter directory: ")
    print(f"Current path: {command}")
    class Server(BaseHTTPRequestHandler):
        returns = subprocess.run(args, shell = True , cwd = command)
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type" , "text/html")
            self.end_headers()
        print(returns)
    server1 = HTTPServer((host , port) , Server)
    server1.serve_forever()
    server1.server_close()
except KeyboardInterrupt as k:
    print("\nServer is closed")
except OSError as e:
    print(f"Error occurred: {e}")