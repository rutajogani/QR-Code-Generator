import http.server
import json


class AdvancedAPIHandler(http.server.BaseHTTPRequestHandler):
    # Handle incoming data from JavaScript
    def do_POST(self):
        # 1. Read the length of the incoming data
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)

        # 2. Parse the JSON data received from JavaScript
        received_json = json.loads(post_data.decode("utf-8"))
        print(f"Python received data: {received_json}")  # Prints in terminal

        # 3. Send a response back to JavaScript
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        response_data = {"status": "Received!", "your_data": received_json}
        self.wfile.write(json.dumps(response_data).encode("utf-8"))


def run():
    print("Server starting on http://localhost:8000 ...")
    http.server.HTTPServer(("", 8000), AdvancedAPIHandler).serve_forever()


if __name__ == "__main__":
    run()
