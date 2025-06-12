from main import CurrencyRates
from controllers import CurrencyRatesCRUD, ViewController


def main():
    # Инициализация с поддержкой только USD, EUR, GBP
    c_r = CurrencyRates(['USD', 'EUR', 'GBP'])
    
    # Обновляем курсы валют
    if not c_r.update_rates():
        print("Не удалось обновить курсы валют")
        return

    # Инициализация контроллера БД
    crud = CurrencyRatesCRUD(c_r)
    
    # Запись данных в БД
    if not crud.create():
        print("Не удалось записать данные в БД")
        return

    # Вывод информации
    view = ViewController(c_r)
    print(view())

    # Закрытие соединения с БД
    crud.close()

if __name__ == "__main__":
    main()