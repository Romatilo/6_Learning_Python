# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали
# билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых
# трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# Вариант решения №1 - строковый
ticket = input("Введите номер вашего билета -> ")
if (ticket[:3] == ticket[3:]):      # Cразу сравним половины наших строк
    print("Поздравляем, вам выпал счастливый билет! Съешьте его.")
else:
    print("Какая жалость, ваш билет не счастливый. Купите еще один и вам, быть может, повезет!")

# Вариант решения №2 - арифметический
ticket = int(input("Введите номер вашего билета -> "))
second_half = 000
first_half = 000
 # разумеется, правильнее было ввести просто "0", но так удобнее для читаемости кода

for i in range(3):
    second_half += ticket % 10 * 10 ** i    # Записываем послежние три числа
    ticket //= 10                           # Отбрасываем число справа

# У нас отслось три числа слева билета. Повторим цикл для первой половины билета:
for i in range(3):
    first_half += ticket % 10 * 10 ** i
    ticket //= 10

if (second_half == first_half):
    print("Поздравляем, вам выпал счастливый билет! Съешьте его.")
else:
    print("Какая жалость, ваш билет не счастливый. Купите еще один и вам, быть может, повезет!")
