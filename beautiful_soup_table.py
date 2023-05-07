from bs4 import BeautifulSoup
import requests

if __name__=='__main__':
	url = 'https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.Y7_MFhVBxPY'
	headers = requests.utils.default_headers()
	req = requests.get(url, headers)
	data = BeautifulSoup(req.content, 'html.parser')
	print(data.prettify())
	table = data.find(id='current_conditions_detail')
	rows = data.find_all('tr')
	for x in rows:
		temp = x.find('b').get_text()
		td = x.find_all('td')
		temp_text = td[1].get_text()
		print('{}:{}'.format(temp, temp_text))