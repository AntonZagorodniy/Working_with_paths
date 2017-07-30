# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os


def get_current_dir():
    migrations = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.join(current_dir, migrations)
    os.chdir(current_dir)
    return current_dir

sql_list = []

def get_sql_list():
    current_dir = get_current_dir()
    file_list = os.listdir(current_dir)
    # sql_list = []
    for file in file_list:
        if (file.find('sql') != -1):
            sql_list.append(file)
        else:
            continue
    return sql_list


def get_new_list(in_string, s_list):
    new_sql_list = []
    for i, file in enumerate(s_list):
        with open(s_list[i], encoding='utf-8-sig') as file:
            for l in file:
                tempstr = l.strip()
                if in_string in tempstr:
                    new_sql_list.append(s_list[i])
        new_sql_set = set(new_sql_list)
        new_sql_set = sorted(new_sql_set)
        sql_list = list(new_sql_set)
    return sql_list


if __name__ == '__main__':
    get_sql_list()
    while True:
        # new_list1 = get_new_list(input_string)
        input_string = input("Введите нужную строку или q - для выхода):\n")
        if input_string == "q":
            break
        else:
            new_list = get_new_list(input_string, sql_list) 
        print(new_list)
        print("Колличество элементов:", len(new_list))