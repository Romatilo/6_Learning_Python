# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#      4

def sum(x, y):
    if y == 0:
        return x
    return (sum(x, y-1))+1


a = int(input("Введите число a -> "))
b = int(input("Введите число b -> "))

print('Сумма числе а и b ->', sum(a, b))