import socket
import ssl

from constants import *
from header import HeaderBuilder

FILE_SCHEME_IDENTIFIER = ":///"
NORMAL_SCHEME_IDENTIFIER = "://"


class URL:
    def __init__(self, url):
        self.scheme, url_without_scheme = url.split(NORMAL_SCHEME_IDENTIFIER, 1)
        assert self.scheme in [HTTP_SCHEME, HTTPS_SCHEME, FILE_SCHEME]

        if self.scheme == FILE_SCHEME:
            self.host = url_without_scheme
            return

        # scheme
        if self.scheme == HTTP_SCHEME:
            self.port = HTTP_PORT
        elif self.scheme == HTTPS_SCHEME:
            self.port = HTTPS_PORT

        # split into host and path
        if "/" not in url_without_scheme:
            url_without_scheme += "/"

        self.host, url_without_scheme = url_without_scheme.split("/", 1)

        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)

        self.path = "/" + url_without_scheme

    def get(self, name):
        return self.__getattribute__(name)

    def request(self):
        if self.scheme == FILE_SCHEME:
            return self._handle_file_scheme()

        s = socket.socket(
            family=socket.AF_INET, type=socket.SOCK_STREAM, proto=socket.IPPROTO_TCP
        )

        if self.scheme == HTTPS_SCHEME:
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=self.host)

        s.connect((self.host, self.port))

        request = f"GET {self.path} HTTP/1.1{LINE_BREAK}"

        header_builder = HeaderBuilder(self.host)
        request += header_builder.build()

        s.send(request.encode("utf8"))

        response = s.makefile("r", encoding="utf8", newline="\r\n")
        status_line = response.readline()
        version, status, explanation = status_line.split(" ", 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line == "\r\n":
                break
            header, value = line.split(":", 1)
            response_headers[header.casefold()] = value

        assert "trasnfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers

        body = response.read()
        s.close()
        return body

    def _handle_file_scheme(self):
        with open(self.host) as f:
            return f.read()
