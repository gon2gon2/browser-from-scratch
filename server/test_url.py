from url import URL

def test_url_support_http_only():
    url = URL("http://asdasd.com")
    assert url.get('scheme') == 'http'
    assert url.get('host') == 'asdasd.com'
    assert url.get('path') == '/'


def test_request():
    url = URL('http://example.org')
    url.request()