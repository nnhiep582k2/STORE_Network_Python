from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
    headers = requests.utils.default_headers()
    url = 'https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Y7_MFhVBxPY'
    req = requests.get(url, headers)
    s = BeautifulSoup(req.content, 'html.parser')
    ngay = s.find(id='seven-day-forecast')
    dubao = ngay.find_all(class_="tombstone-container")
    tonight = dubao[0]
    img = tonight.find('img')
    mota = img['title']
    d = []
    for i in range(len(dubao) - 1):
        tonight = dubao[i]
        period = tonight.find(class_='period-name').get_text()
        shortdesc = tonight.find(class_='short-desc').get_text()
        temp = tonight.find(class_="temp").get_text()
        img = tonight.find('img')['title']
        d.append((period, shortdesc, temp, img))
    for i in range(len(d) - 1):
        print(d[i])