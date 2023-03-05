# Написать функцию для нахождения наибольшего общего делителя двух чисел:

def nod(x, y):
    if not(x != 0 and y != 0):
        return x + y
    else:
        if x > y:
            return nod(x % y, y)
        else:
            return nod(x, y % x)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

print(nod(a, b))