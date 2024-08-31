# Если введенное имя совпадает с “Вячеслав”, то вывести “Привет, Вячеслав”, если нет, то вывести "Нет такого имени"
expectedName = False

while not expectedName:
    name = input("Введите  имя: ")
    if name == 'Вячеслав' :
        print("Привет, Вячеслав")
        expectedName = True
    else:
        print("Нет такого имени")