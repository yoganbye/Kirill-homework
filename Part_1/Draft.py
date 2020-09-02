import os


def read_file():
    path1 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'workers')
    path2 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'hours_of')

    with open(path1, 'r+', encoding='utf-8') as file:
        list_norm = file.read().split('\n')

    with open(path2, 'r+', encoding='utf-8') as file1:
        list_real = file1.read().split('\n')
    return list_norm, list_real



