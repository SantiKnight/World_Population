def get_population(country_dict):
    population_dict = {
        '2022': float(country_dict['2022 Population']),
        '2020': float(country_dict['2020 Population']),
        '2015': float(country_dict['2015 Population']),
        '2010': float(country_dict['2010 Population']),
        '2000': float(country_dict['2000 Population']),
        '1990': float(country_dict['1990 Population']),
        '1980': float(country_dict['1980 Population']),
        '1970': float(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values 

def get_population_by_country(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))
    

def get_population_porcentile(data):
    population_dict = {item["Country/Territory"]:item['World Population Percentage'] for item in data} 
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values