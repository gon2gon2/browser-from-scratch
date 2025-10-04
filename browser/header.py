class HeaderBuilder:
    __line_break = "\r\n"
    __headers = {}

    def __init__(self, host, user_agent=None):
        self.__headers["Host"] = host

        if user_agent:
            self._add_header("User-Agent", user_agent)

    def build(self):
        header_string = ""
        for k, v in self.__headers.items():
            header_string += f"{k}: {v}"
            header_string += self.__line_break

        header_string += self.__line_break
        return header_string

    def _add_header(self, h, v):
        self.__headers[h] = v
