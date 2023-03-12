# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

# Функция формирования списка.
def Form_array(amount, min_element, max_element):
    list_array = []
    for i in range(amount):
        list_array.append(random.randint(min_element, max_element))
    return list_array

# Функция определения индексов массива, входящих в заданный диапазон.
def List_of_indexes_in_range(array, min, max):
    list_of_indexes = []
    for i in range(len(array)):
        if min <= array[i] <= max:
            list_of_indexes.append(i)
    return list_of_indexes


lengthArray = int(input("Задайте количество элементов массива -> "))
a, b = map(int, input("Задайте диапазон искомых чисел через пробел -> ").split(" "))

list_array = Form_array(lengthArray, 1, 10)
print(list_array)

print("Индексы элементов массива в заданном вами диапазоне -> ",
      List_of_indexes_in_range(list_array, a, b))