# d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
# С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d. Функция должна возвращать новый созданный одномерный список.

def get_line_list(d):
    if (d == []):
        return d
    if isinstance(d[0], list):
        return(get_line_list(d[0]) + get_line_list(d[1:]))
    return(d[:1] + get_line_list(d[1:]))

d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
print(get_line_list(d))
