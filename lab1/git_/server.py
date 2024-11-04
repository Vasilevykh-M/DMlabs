from http.server import BaseHTTPRequestHandler

from threading import Thread
from wsgiref.simple_server import make_server



class Server(BaseHTTPRequestHandler):
    def __init__(self):
        self._thread = Thread(target=self._run)
        self._code = ""


    def _app(self, environ, start_response):
        headers = [('Content-type', 'text/plain; charset=utf-8')]

        for arg in environ["QUERY_STRING"].split("&"):
            if arg.split("=")[0] == "code":
                status = '200 OK'
                start_response(status, headers)
                self._code = arg.split("=")[-1]
                return ["Ок. Возвращайтесь к вашему приложению".encode()]

        status = "400 Bad Request"
        start_response(status, headers)
        return ["Ошибка. Повторите попытку снова".encode()]


    def _run(self):
        with make_server('', 8000, self._app) as httpd:
            httpd.handle_request()


    def start(self):
        self._thread.start()


    def get_code(self):
        self._thread.join()
        return self._code