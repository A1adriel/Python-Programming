def remainder(N0, t, t_half):
    """Вычисляем остаток радиоактивного вещества."""
    return N0 * (1 / 2) ** (t / t_half)

def curry(t_half):
    """Создаем каррированную функцию с фиксированным периодом полураспада."""
    return lambda N0, t: remainder(N0, t, t_half)

#Словарь изотопов и их периодов полураспада
isotopes = {
    "C-14": 5730,    
    "U-238": 4500000000, 
    "K-40": 1261000000,
}

#Создаем словарь каррированных функций
carr_funcs = {isotope: curry(t_half) for isotope, t_half in isotopes.items()}

#Исходные данные
N0 = 1000  
t = 1000   

#Цикл по каррированным функциям и вывод результата
for isotope, func in carr_funcs.items():
    remaining = func(N0, t)
    print(f"{isotope}: Остаток после {t} лет = {remaining:.2f}")