from url import URL

if __name__ == '__main__':
    url = URL('http://example.org')
    res = url.request()

    print(res)