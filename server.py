import http.server
import json


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(changeUrlToQrCode):
        self.send_response(200)
        
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()


def run():
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    print("Python server running on http://localhost:8000 ...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
