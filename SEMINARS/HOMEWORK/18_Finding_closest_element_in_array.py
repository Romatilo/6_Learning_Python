# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

lengthArray = int(input("Задайте длину массива -> "))
n = int(input("Масив состоит из натуральных чисел 1..N. Введите N -> "))
x = int(input("Введите число X -> "))
listNumber = []
for i in range(lengthArray):
    listNumber.append(random.randint(1, n))
print(listNumber)

# Объявим две переменные: closest хранит ближайший к Х элемент
#                         difference - разницу между X и ближайшим элементом (по модулю)
closest = listNumber[0]                 
difference = abs(listNumber[0] - x)

# В цикле проверим разницу между каждым элементом и X. Если разница меньше предыдущей, 
# присвоим переменной closest значение проверяемого элемента.
for i in listNumber:
    if abs (i-x) < difference:
        difference = abs (i-x)
        closest = i

print (f'Ближайшее к числу X = {x} число в массиве: {closest}')