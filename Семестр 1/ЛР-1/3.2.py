def guess_number(number, low, high):
    """Функция угадывания числа"""
    n = low
    result = 0
    while n <= high:
        result += 1
        if n == number:
            return n, result
        n += 1
    return None, result

def test1():
    """Первый тест с неправильным результатом"""
    num, result = guess_number(10, 1, 9)
    assert result == 10
    
def test2():
    """Второй тест с правильнмы результатом"""
    num, result = guess_number(5, 1, 10)
    assert result == 7

def main():
    #Ввод числа
    number = int(input("Загадайте число: "))
    
    #Ввод нижней и верхней границы поиска числа
    low = int(input("Введите нижнюю границу: "))
    high = int(input("Введите верхнюю границу: "))
    
    #Вызов функции угадывания числа
    num, result = guess_number(number, 1, 100)
    
    #Вывод результата
    if num is not None:
        print(f"Угадано число: {num} за {result} попыток.")
    else:
        print("Число не угадано")

if __name__ == "__main__":
    main()
    test1()
    test2()