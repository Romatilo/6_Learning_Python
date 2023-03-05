# Написать функцию вычисления факториала числа n:

def factorial(n):
    fact = n
    if n == 0:
        return(1)
    return (n * factorial(n-1))

print (factorial (5))