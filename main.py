import http.server
import json

import qrcode as qr


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(changeUrlToQrCode):
        
        url = input("Enter the URL: ")
        img = qr.make(url)
        print("---QR Code is Generator---")

        getUrl = urlparse(self.url
        
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
