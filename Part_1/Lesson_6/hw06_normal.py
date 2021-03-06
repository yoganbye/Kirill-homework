# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
'''
def avg(a, b):
    #"""Вернуть среднее геометрическое чисел 'a' и 'b'.

    #Параметры:
    #    - a, b (int или float).

    #Результат:
     #   - float.
    #"""
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))

'''

# Задача-2:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

print('1. Перейти в папку', '2. Просмотр содержимого', '3. Удалить папку', '4. Создать папку', sep='\n')
print()
try:
    call = int(input('Введите число: '))
except ValueError:
    print('Введите число корректно')

import os, hw06_easy, sys

def change_dir(path):
    #Функция смены дирректории
    try:
        path_name = input('Ввидите имя папки: ')
        os.chdir(os.path.join(os.getcwd(), path_name))
    except Exception:
        print('Такой папки нет')

    print(os.getcwd())

def del_dir():
    try:
        from os import rmdir
        name_dir = input('Введите имя папки на удаление: ')
        os.rmdir(name_dir)

    except FileNotFoundError:
        print('Не удается найти файлы')

def create_dir():
    try:
        name_dir = input ('Введите имя создаваемой папки: ')
        os.mkdir(name_dir)

    except FileExistsError:
        print('Невозможно создать фалы, т.к. они существуют')


if call == 1:
    try:
        change_dir(input('Введите путь: '))
    except FileNotFoundError:
        print("Не удается найти указанный файл")
    
elif call == 2:
    #импорт функции просмотра содержимого
    hw06_easy.view_content_dir()

elif call == 3:
    del_dir()

elif call == 4:
    create_dir()

else:
    print('Выбрано не корректное действие')
