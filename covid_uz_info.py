from covid import Covid

covid = Covid(source="john_hopkins")

# to get data from worldometers.info
covid = Covid(source="worldometers")


def get_stat():
    data = covid.get_data()
    my_country = {}
    for x in data:
        if x['country'] == 'Uzbekistan':
            my_country.update(x)
    
    # try:
    country = my_country['country']
    conf = my_country['confirmed']
    new_cases = my_country['new_cases']
    deaths = my_country['deaths']
    recovered = my_country['recovered']
    active = my_country['active']
    new_deaths = my_country['new_deaths']
    ls = [country,conf,new_cases,deaths, recovered,active, new_deaths]
    print(ls)
    # except Exception as error:
    #     print('#'*25, error)
    return True
get_stat()