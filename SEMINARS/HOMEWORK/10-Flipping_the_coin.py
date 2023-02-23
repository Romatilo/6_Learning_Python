# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть






import random

tails_counter = 0       # Нет необходимости хранить количество решек и гербов в отдельной переменной, достаточно одной.
n = int(input("Задайте общее количество монет -> "))
for i in range(n):              # сгенерируем последовательность нолей и единиц (решек и гербов)
    coin = random.randint(0,1)
    if coin == 0:
        tails_counter += 1               # и втом же цикле сосчитаем количество решек
        print (i, "Решка")
    else: 
        print (i, "Герб")                # объявляем, что выпал герб, но считать его ни к чему  
if (tails_counter < n/2):                
    print(f"Вам нужно перевернуть {tails_counter} Решек")       
else:
    print(f"Вам нужно перевернуть {n - tails_counter} Гербов")

# Окончаниями слов Гербов и Решек не стал "заморачиваться", чтобы не усложнять программу.