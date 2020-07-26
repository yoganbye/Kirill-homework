

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def make_dir():
    '''
    функция создает девять директорий
    '''
    try:
        from os import mkdir
        for i in range(9):
            mkdir(f'dir{i+1}')

    except FileExistsError:
        print('Невозможно создать фалы, т.к. они существуют')

def del_dir():
    '''
    функция удаляет девять директорий
    '''
    try:
        from os import rmdir
        for i in range(9):
            rmdir(f'dir{i+1}')

    except FileNotFoundError:
        print('Не удается найти файлы')


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.


def view_content_dir():
    '''
    функция отображает папки текущей директории
    '''
    import os
    path = os.listdir(os.getcwd())
    print(path)


# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():
    '''
    функция создает копию текущего файла
    '''
    import os, sys
    
    path = os.path.join(os.getcwd(), sys.argv[0])
    with open(f'{path}_copy', 'w', encoding='utf-8') as file:
        pass
