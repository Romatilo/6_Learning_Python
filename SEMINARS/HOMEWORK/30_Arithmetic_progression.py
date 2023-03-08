# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_term = int(input("Введите первый элемент прогрессии -> "))
difference = int(input("Введите разность между элементами -> "))
n = int(input("Введите номер требуемого члена прогрессии, n -> "))

# Через цикл:
list_Arithmetic_progression = []
for i in range (1,n+1):
    list_Arithmetic_progression.append(first_term + (i-1)*difference)

print(list_Arithmetic_progression)

# Через рекурсию
def Arithmetic_progression (a1, d, n, list_AP = []):
    if n == 0:
        return list_Arithmetic_progression
# Добавлять члены прогрессии в список будем в обратном порядке, каждый раз в начало списка
    list_AP.insert(0, (a1 + (n-1) * d))
    return Arithmetic_progression (a1, d, n-1)

list_AP_recursion = Arithmetic_progression(first_term, difference, n)
print (list_AP_recursion)

if (list_Arithmetic_progression == list_AP_recursion):
    print ("Способы решения дали равный результат.")
else: print("Учись усерднее, студент!")