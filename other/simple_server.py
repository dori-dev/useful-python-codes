"""simple server write in python
"""
from http.server import BaseHTTPRequestHandler, HTTPServer

HTML_CODES = """
<h1>Hello There</h1>
<h3>Welcome</h3>
<p>This is my custom server</p>
"""

host_name, server_port = 'localhost', 8080


class Server(BaseHTTPRequestHandler):
    """the server module
    """
    def do_GET(self):
        """get method"""
        self.send_response(200)
        self.end_headers()
        self.wfile.write(
            bytes(HTML_CODES, 'utf-8'))


if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port), Server)

    try:
        print(f'open with your browser: http://{host_name}:{server_port}/')
        web_server.serve_forever()
        web_server.server_close()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        print(err)
    print('server closed...')
