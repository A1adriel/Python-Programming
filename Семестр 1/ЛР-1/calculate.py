def calculate(num1, num2, choice):
    if choice == '+':
        print('Результат:', num1 + num2)
    elif choice == '-':
        print('Результат:', num1 - num2)
    elif choice == '*':
        print('Результат:', num1 * num2)
    elif choice == '/':
        if num2 != 0:
            print('Результат:', num1 / num2)
        else: 
            print('Невозможно разделить на 0')

def test_add():
    """Тест операции сложения"""
    assert calculate(5.0, 5.0, "+") == 10.0
def test_subtract():
    """Тест операции вычитания"""
    assert calculate(5, 5, "-") == 0
def test_multiply():
    """Тест операции умножения"""
    assert calculate(5, 5, "*") == 25
def test_divide():
    """Тест операции деления"""
    assert calculate(5, 5, "/") == 1

def main():        
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    choice = input("Введите тип арифметической операции: ")
    calculate(num1, num2, choice)
if __name__ == "__main__":
    main()
    test_add()
    test_subtract()
    test_multiply()
    test_divide()