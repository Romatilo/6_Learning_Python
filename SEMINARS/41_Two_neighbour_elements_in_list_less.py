

n = int(input('Введите количество элементов первого множества -> '))
list_one = list()
for i in range (n):
    list_one.append(int(input(f'Введите число {i+1} первого множества -> ')))

print(list_one)

result = 0
for i in range (1,len(list_one)):
    if list_one[i] > list_one[i-1] and list_one[i] > list_one[i+1]:
        result += 1

print (result)