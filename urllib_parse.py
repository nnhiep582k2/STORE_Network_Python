from urllib.parse import urlparse, quote

if __name__=='__main__':
    result = urlparse('https://www.python.org/')
    data = quote('nnhiep hihi')
    print(result)