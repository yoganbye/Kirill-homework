# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

from random import randint
import re

try:
    file = open('Part №1\Lesson №5\work3.txt', 'w+')

    try:
        for i in range(2500):
            file.write(str(randint(0, 9)))

        file.seek(0)

        a = file.read()
        
        print(a)
        print()
        
        tmp = ''
        maximum = ''
        for i in range(len(a) - 1):
            if len(tmp) == 0 and (a[i] == a[i+1] or a[i] == a[i-1]):
                tmp += a[i]
            elif (a[i] == a[i+1] or a[i] == a[i-1]) and a[i] in tmp:
                tmp += a[i]
            elif len(tmp) > len(maximum):
                maximum = tmp
                tmp = ''
            else:
                tmp = ''
    
        print(maximum)

    finally:
        file.close()

except FileNotFoundError:
    print('Не возможно прочесть')


