# Список (list) - через квадратные скобки.

# создание нового списка
list_1 = []

# или через функцию
list_1 = list()
print (list_1)

# узнвть длину списка
print(len(list_1))

# Добавить в список ОДИН элемент
list_1.append(8)
list_1.append(85)
list_1.append(85)
print (list_1)

# Удалить элемент из списка. 
# Последний
list_1.pop()
print (list_1)

# Заданный
list_1.pop(0)
print (list_1)

# Вставить в список в определенную позицию
list_1.insert(1,55)
print (list_1)

# Кортеж (tuple)- неизменяемы список.
# задается через круглые скобки
tuple_1 = (12,54,0,)
print(tuple_1)
print(type(tuple_1))

# Можно преобразовать список в кортеж и наоборот.
tuple_1 = list(tuple_1)
print(type(list_1))

