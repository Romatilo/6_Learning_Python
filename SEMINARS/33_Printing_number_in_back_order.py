# 1. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.

def number(n):
    if n == 1 : 
        return (print(1))
    print (n)
    return number (n - 1)
number(10)
