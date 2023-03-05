# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один 4заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# Получается, модуль собирает одновременно ягоды с грядок i, i-1, i+1
# В следующем проходе: i+1, i-1+1, i+1+1, т.е. i+1, i, i+2

# Пусть число кустов n задает пользователь
# А количество ягод на каждом кусту задается рандомно

import random

n = int(input("Введите общее количество кустов -> "))
a = list()

for i in range(n):
    # Допустим, урожайность куста от 100 до 1000 ягод:
    a.append(random.randint(100, 1000))

print("Количество ягод на каждом кусту -> ", a)
# Т.к. кусты замкнуты по кругу, необходимо учесть первые два куста при подсчете урожая с двумя послденими
a.extend((a[0],a[1]))

max = 0

for i in range(1, n+1):   # У нас стало n+2 элементов в списке
    if (a[i]+a[i-1]+a[i+1]) > max:
        max = a[i]+a[i-1]+a[i+1]

print("Максимальное количество ягод, котое может собрать модуль за один заход -> ", max)