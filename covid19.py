# importing modules
import requests
from bs4 import BeautifulSoup

# URL
url = 'https://coronavirus.uz/ru'

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

data = []

confirmed = soup.findAll('p', class_='prg-count')
for c in confirmed:
    done = c.get('data-count')
    data.append(done)

print(f"Всего подтверждено = {data[0]}")
print(f"Выздоровевшие = {data[1]}")
print(f"Умершие = {data[2]}")
print(f"На лечении = {data[3]}")
