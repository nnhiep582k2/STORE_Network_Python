from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
from datetime import datetime

if __name__=='__main__':
    cookie_jar = CookieJar()
    opener = build_opener(HTTPCookieProcessor(cookie_jar))
    opener.open('https://github.com')
    cookies = list(cookie_jar)
    print(cookies)
    print(len(cookies))
    print(cookies[0].name)
    print(cookies[0].value)
    print(cookies[0].path)
    print(cookies[0].domain)
    print(cookies[0].secure)
    print(cookies[0].expires)
    print(datetime.fromtimestamp(cookies[0].expires))