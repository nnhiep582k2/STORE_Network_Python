import requests

if __name__=='__main__':
    url = 'https://www.w3schools.com/python/demopage.htm'
    req = { 'nnhiep': 21 }
    #r = requests.get(url)
    #r = requests.get(url, auth = { 'user', 'password' })
    r = requests.post(url, req)
    print(r.text)

import requests

if __name__=='__main__':
    query = { 'q': 'river', 'order': 'popular', 'min_width': '800', 'min_height': '600' }
    url = 'https://pixabay.com/vi/photos/'
    req = requests.get(url, query)
    print(req.url)