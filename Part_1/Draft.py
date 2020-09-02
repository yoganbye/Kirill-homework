# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

import os
import json
import pickle

dikt_fruts = dict()

path = os.path.join('G:\Python\Work Folder\Kirill-homework\Part_1\Lesson_4\data', 'fruits.txt')
with open(path, encoding='utf-8') as inp_ut:
    for fruits in inp_ut.readlines():
        if fruits == '\n':
            continue
        file_name = 'fruits_{}'.format(fruits[0].upper())
        dikt_fruts[file_name] = dikt_fruts.get(file_name,'') + fruits


for i in dikt_fruts:
    name = '{}.txt'.format(i)
    with open(name,'w', encoding='utf-8') as out:
        out.write(dikt_fruts[i])
print('Finish')



