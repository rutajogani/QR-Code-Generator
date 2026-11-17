import http.server
from urllib.parse import urlparse, parse_qs
import qrcode
import io

class QRHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        
        if parsed_url.path == "/generate":
            query_params = parse_qs(parsed_url.query)
            target_url = query_params.get("url", [None])[0]

            if target_url:
                # Generate QR code
                img = qrcode.make(target_url)
                
                # Save to buffer
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                buffer.seek(0)

                # Send back to browser as an image
                self.send_response(200)
                self.send_header("Content-Type", "image/png")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(buffer.read())
                return

        self.send_response(404)
        self.end_headers()

def run():
    server_address = ("", 8000)
    httpd = http.server.HTTPServer(server_address, QRHandler)
    print("Python server running on http://localhost:8000 ...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
