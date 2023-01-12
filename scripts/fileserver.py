import http.server
import socketserver

HOST = '127.0.0.1'
PORT = 8000
# DIRECTORY = "../"

# class Handler(http.server.SimpleHTTPRequestHandler):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, directory=DIRECTORY, **kwargs)

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print("Serving HTTP on " + str(HOST) + " port " + str(PORT) + " (http://" + str(HOST) + ":" + str(PORT) + "/)")
    httpd.serve_forever()