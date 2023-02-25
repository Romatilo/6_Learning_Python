# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] ответ 6

import random

number = int(input())
listNumber = []
for i in range(number):
    listNumber.append(random.randint(-3, 3))
print(listNumber)

# # Способ 1: Смена типа переменной

# listNumber = set(listNumber)
# print(listNumber)

# Способ 2: перебираем элементы списка

newList = [listNumber[0]]
for j in range( len(listNumber) ):
    flag = True
    for k in range( len(newList) ):
        if newList[k] == listNumber[j]:
            flag = False
            break
    if flag:
        newList.append( listNumber[j] )
print(newList)

# # Способ 3

# newList = []
# for i in listNumber:
#     if i not in newList:
#         print(i)
#         newList.append(i)
#         print(newList)
# print(newList)