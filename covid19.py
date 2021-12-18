# importing modules
# pip install bs4
import requests
from bs4 import BeautifulSoup as bs

# URL
url = 'https://coronavirus.uz/ru'

# get URL html
page = requests.get(url)
soup = bs(page.text, 'html.parser')



def get_data():
	data = []	
	confirmed = soup.findAll('p', class_='prg-count')
	for c in confirmed:
	    done = c.get('data-count')
	    data.append(done)
	return data


print(f"Всего подтверждено = {data[0]}")
print(f"Выздоровевшие = {data[1]}")
print(f"Умершие = {data[2]}")
print(f"На лечении = {data[3]}")
