# -- Readonly
from urllib.request import urlopen
import urllib.error

if __name__=='__main__':
    try:    
        response = urlopen("https://www.python.org/")
        #data = response.read()
        #data = response.readline()
        #data = response.url
        #data = response.status
        data = response.getheaders()
        print(data)
    except urllib.error.HTTPError as e:
        print(e)

# -- change header
from urllib.request import Request
import gzip

if __name__=='__main__':
    try:
        request = Request('https://www.python.org/')
        #request.add_header('Accept-Language', 'vi')
        request.add_header('Accept-Encoding', 'gzip')
        response = urlopen(request)
        #content = gzip.decompress(response.read())
        #print(content.splitlines()[:5])
        print(response.getheader('Content-Encoding'))
        #print(response.getheader('User-agent'))
    except urllib.error.HTTPError as e:
        print(e)
        
# -- redirect
from urllib.request import Request, urlopen

if __name__=="__main__":
    url = 'http://www.gmail.com'
    req = Request(url)
    r = urlopen(req)
    print(req.redirect_dict)