pip install covid 
from covid import Covid

covid = Covid(source="john_hopkins")

# to get data from worldometers.info
covid = Covid(source="worldometers")

# get all data
data = covid.get_data()
my_country = {}
for x in data:
	if x['country'] == 'Uzbekistan':
		my_country.update(x)
for i in my_country.items():
	print(i)