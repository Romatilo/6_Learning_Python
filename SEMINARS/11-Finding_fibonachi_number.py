# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, 
# выведите число -1.

# F n = F n − 1 + F n − 2 .

def fib(n: int)->int:
    old_n = 0
    new_n = 1
    fib = 0
    for i in range(n-1):
        fib = old_n + new_n
        old_n, new_n = new_n, fib
    return fib

number = int(input("Введите натуральное число -> "))
temp = 

flag =True
i = 1
while(flag):
    if t10.fib(i) < number:
        i+=1
    elif t10.fib(i) == number:
        print(i)
        flag = False
    else:
        print(-1)
        flag = False