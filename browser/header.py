from constants import LINE_BREAK


class HeaderBuilder:
    def __init__(self, host):
        self.__header = {}

        self._add_header("Host", host)

    def user_agent(self, v):
        self._add_header("User-Agent", v)

    def build(self):
        header = ""
        for k, v in self.__header.items():
            header += f"{k}: {v}{LINE_BREAK}"

        return header + LINE_BREAK

    def _add_header(self, h, v):
        self.__header[h] = v
