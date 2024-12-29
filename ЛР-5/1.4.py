import csv

countries = {}

with open('world-cities.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i in reader:
        if i["country"] not in countries.keys():
            countries[i["country"]] = [i["name"]]
        else:
            countries[i["country"]].append(i["name"])

while True:
    cities_to_find= input("Введите города для поиска (через пробел): ").split()
    for city_to_find in cities_to_find:
        for country, cities in countries.items():
            if (city_to_find.lower() in [city.lower() for city in cities]):
                print(f"{city_to_find} находится в {country}")