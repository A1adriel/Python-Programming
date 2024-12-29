import requests
from bs4 import BeautifulSoup

url = "https://yandex.com.am/weather"
response = requests.get(url)

bs = BeautifulSoup(response.text,"lxml")
temp = bs.find('span', 'temp__value temp__value_with-unit')
summary = bs.find('div', 'title-icon__text');
print(f"Температура: {temp.text}")
print(f"{summary.text}")