
# Если введенное число больше 7, то вывести “Привет”

expectedValue = False

while not expectedValue:
    number = int(input("Введите число: "))
    if number > 7:
        print("Привет")
        expectedValue = True

