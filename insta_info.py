import requests
from bs4 import BeautifulSoup

url = 'https://ziyouz.uz/hikmatlar/aforizmlar/azmu-jazm-bilan-ish-tut-amir-temur-ogit-va-yoriqlaridan/'
# user = str(input('Your username :'))
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

publications = soup.findAll('p')
res = []
for p in publications:
	res.append(p.text.strip())

for afo in res:
	print(afo)