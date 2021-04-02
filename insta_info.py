from bs4 import BeautifulSoup, Tag
import requests

from collections import defaultdict

def find_most_common():
	page = requests.get("https://en.wikipedia.org/wiki/Apple_Inc.")
	soup = BeautifulSoup(page.text, "html.parser")
	print(soup.text)

find_most_common()