import matplotlib.pyplot as plt
import numpy as np
import requests

def f1(x):
    return 1/x

def f2(x):
    return np.cos(x)

def get_weather_data(format):
    url = f"https://wttr.in/?format={format}"
    try:
        response = requests.get(url) 
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка при запросе к серверу: {e}")
        return None


fig1, ax1 = plt.subplots(figsize=(10, 6))
x = np.linspace(-np.pi, np.pi, 400)
ax1.plot(x, f1(x), label='y = 1/x')
ax1.plot(x, f2(x), label='y = cos(x)')
ax1.set_title('Графики двух функций')
ax1.legend()

weather_data= get_weather_data("j2")
dates = list()
temps = list()

for weather_info in weather_data['weather']:
    dates.append(weather_info['date'])
    temps.append(int(weather_info['avgtempC']))

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(dates, temps)
ax2.set_title('График средней температуры на 3 дня')
ax2.set_xlabel('Дата')
ax2.set_ylabel('Средняя температура (°C)')
ax2.grid(True) 

plt.show()