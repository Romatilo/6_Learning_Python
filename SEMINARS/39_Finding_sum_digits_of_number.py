# Написать функцию для нахождения суммы цифр числа:

def Finding_digits_sum(n,sum=0):
    if n // 10 == 0:
        return sum + n % 10
    return Finding_digits_sum(n//10, (sum+n%10))

print (Finding_digits_sum(4408935))

# Немного по-другому:

def Finding_digits_sum(n):
    if (n // 10) == 0:
        return n % 10
    return Finding_digits_sum(n//10) + n % 10

print (Finding_digits_sum(4408935))