def function_1(a, b):
    def function_2():
        print(a, b)
    
    #Возвращаем внутреннюю функцию
    return function_2

#Использование
function = function_1('Python', 'IITTO')
function()  # Выведет "Python IITTO"