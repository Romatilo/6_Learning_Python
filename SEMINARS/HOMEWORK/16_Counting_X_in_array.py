# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random

lengthArray = int(input("Задайте длину массива -> "))
n = int(input("Масив состоит из натуральных чисел 1..N. Введите N -> "))
x = int(input("Введите число X -> "))
listNumber = []
for i in range(lengthArray):
    listNumber.append(random.randint(1, n))
print(listNumber)

counter = 0
for i in listNumber:
    if i == x:
        counter += 1
print (f'Число {x} встречается в массиве {counter} раз')
