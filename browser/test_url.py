from url import URL
from constants import *


def test_url_support_http():
    url = URL("http://asdasd.com/path")
    assert url.get("scheme") == HTTP_SCHEME
    assert url.get("port") == HTTP_PORT
    assert url.get("host") == "asdasd.com"
    assert url.get("path") == "/path"


def test_url_support_https():
    url = URL("https://asdasd.com/path2")
    assert url.get("scheme") == HTTPS_SCHEME
    assert url.get("port") == HTTPS_PORT
    assert url.get("host") == "asdasd.com"
    assert url.get("path") == "/path2"


def test_url_support_file():
    url = URL(
        "file:///Users/gondev/IdeaProjects/browser-from-scratch/server/sample.txt"
    )
    assert url.get("scheme") == FILE_SCHEME
    assert (
        url.get("host")
        == "/Users/gondev/IdeaProjects/browser-from-scratch/server/sample.txt"
    )
    assert url.request() == "This is sample"
