class HeaderBuilder:
    __line_break = "\r\n"
    __header = ""

    def __init__(self, host):
        self.__headers["Host"] = host

    def user_agent(self, v):
        self._add_header("User-Agent", v)

    def build(self):
        return self.__header + self.__line_break

    def _add_header(self, h, v):
        self.__headers[h] = v
