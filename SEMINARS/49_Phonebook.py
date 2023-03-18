# Иванов,       Иван,       111,       описание Иванова
# Петров,       Петр,       222,       описание Петрова
# Васичкина,       Василиса,       333,       описание Васичкиной
# Питонов,       Антон,       777,       умеет в Питон
# 555,       333,       789,       dfdf


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data


def write_csv(filename: str, data) -> str:
    file = open(filename, 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')


def write_txt(filename: str, data) -> str:
    file = open(filename + ".txt", 'w', encoding='utf-8')
    for lines in data:
        s = ', '.join(f'{v}' for k, v in lines.items())
        file.write(s + '\n')


def get_file_name() -> str:
    name_of_the_file = input(
        'Введите название файла, который вы хотите сохранить -> ')
    return name_of_the_file


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Удалить абонента из справочника\n"
          "6. Сохранить справочник в текстовом формате\n"
          "7. Закончить работу")
    choice = int(input())
    return choice


def print_result(data) -> list:
    print(*data, sep='\n')


def find_by_name(data, sirname) -> str:
    for key in data:
        if key['Фамилия'].upper() == sirname.upper():     
            return key.values()
    return 'Такого пользователя нет!'

def find_by_number(data, telephone_number) -> str:
    for key in data:
        if key['Телефон'] == telephone_number.strip():
            return (key.values())
    return 'Пользователя с таким номером телефона нет!'

def get_new_user() -> dict:
    record = {
        'Фамилия': input('Введите фамилию -> '),
        'Имя': input('Введите имя -> '),
        'Телефон': input('Введите номер телефона -> '),
        'Описание': input('Введите описание -> ')
    }

    return record


def add_user(data: list, new_record) -> list:
    data.append(new_record)
    print(*data,  sep='\n')


def delete_user(data: list, last_name: str) -> str:
    for i in range(len(data)):
        if data[i].get("Фамилия") == last_name:
            del data[i]
            return print (f"Абонент {last_name} успешно удален")
    return print ("Такой абонент отсутствует в списке")


phone_book = read_csv('phonebook.csv')

choice = show_menu()

while (choice != 7):
    if choice == 1:
        print_result(phone_book)
    elif choice == 2:
        name = (input("Введите фамилию абонента -> "))
        print(*(find_by_name(phone_book, name)))
    elif choice == 3:
        number = input("Введите номер телефона абонента -> ")
        print(*(find_by_number(phone_book, number)))
    elif choice == 4:
        user_data = get_new_user()
        add_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 5:
        user_data = input(
            "Введите фамилию пользователя, которого вы хотите удалить -> ")
        delete_user(phone_book, user_data)
        write_csv('phonebook.csv', phone_book)
    elif choice == 6:
        file_name = get_file_name()
        write_txt(file_name, phone_book)
    choice = show_menu()