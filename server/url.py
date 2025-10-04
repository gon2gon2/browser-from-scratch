import socket

class URL:
    def __init__(self, url):
        self.scheme, url = url.split("://", 1)
        assert self.scheme == "http"
        if "/" not in url:
            url += "/"
        self.host, url = url.split("/",1)
        self.path = "/" + url
        

    def get(self, name):
        return self.__getattribute__(name)
    
    def request(self):
        s = socket.socket(
            family=socket.AF_INET,
            type=socket.SOCK_STREAM,
            proto=socket.IPPROTO_TCP
        )
        s.connect((self.host, 80))

        request = f"GET {self.path} HTTP/1.0\r\n"
        request += f"Host: {self.host}\r\n"
        request += "\r\n"
        s.send(request.encode("utf8"))

        response = s.makefile("r", encoding="utf8", newline='\r\n')
        status_line = response.readline()
        version, status, explanation = status_line.split(' ', 2)

        response_headers = {}
        while True:
            line = response.readline()
            if line == '\r\n' : break
            header, value = line.split(':',1)
            response_headers[header.casefold()] = value


        assert "trasnfer-encoding" not in response_headers
        assert "content-encoding" not in response_headers
        
        body = response.read()
        s.close()
        return body