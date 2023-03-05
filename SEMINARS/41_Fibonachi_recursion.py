# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def Fibonachi(n):
    if n in (1, 2):
        return 1
    return Fibonachi(n-1) + Fibonachi(n-2)

n = int(input("Введите номер в последовательности Фибоначчи -> "))
print (f"Значение числа под номером {n} в последовательности Фибоначчи - >", Fibonachi(n))