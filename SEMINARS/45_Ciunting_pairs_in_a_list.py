# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

# n = int(input('Введите количество элементов списка -> '))
list_one = [1,2,2,5,2,5,1]
# for i in range (n):
#     list_one.append(int(input(f'Введите число {i+1} списка -> ')))

print(list_one)

count = 0
for i in range (len(list_one)-1):
    for j in range(i+1, len(list_one)):
        if list_one[i] == list_one[j] and i != j:
            count +=1 
            list.pop(j)
            list_one[j] = -1
            break

print (count)