# 53. Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N, состоящий из нулей, а по главной диагонали - единицы. (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла). Результат вывести в виде таблицы чисел как показано в примере ниже.


# Sample Input:
# 4
# Sample Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# Вариант 1. Мой, длинный
n = int(input("Введите N -> "))
newlist = [[0] * n for i in range(n)]
for i in range(n):
    for j in range (n):
        if i == j:
            newlist[i][j] = 1
        else:
            newlist[i][j] = 0

for rows in newlist:
    print(*rows)

# Вариант 2. Короче
lst = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
for rows in lst:
    
    print(*rows)

# Вариант 3. Булевый.
list = [[int(i==j) for i in range(n)] for j in range (n)]
print(*list, sep = '\n')