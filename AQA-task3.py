 # На входе есть числовой массив, необходимо вывести элементы массива кратные 3

def threeMultiplies (array):
    result = [x for x in array if x % 3 == 0]
    print("Элементы массива, кратные 3:", result)

array = list(map(int, input("Введите числовой массив через пробел: ").split()))
threeMultiplies(array)

