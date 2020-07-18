# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1 = []
a2 = []
a3 = []
a4 = []
a = [a1, a2, a3, a4]

a1.append(input('Введите x1: '))
a1.append(input('Введите y1: '))
a2.append(input('Введите x2: '))
a2.append(input('Введите y2: '))
a3.append(input('Введите x3: '))
a3.append(input('Введите y3: '))
a4.append(input('Введите x4: '))
a4.append(input('Введите y4: '))

# начало части кода, которая ищет все возможные длины отрезков
import math
def vector_len(a1, a2):
    vectorlen = math.sqrt((int(a1[0]) - int(a2[0])) ** 2 + (int(a1[1]) - int(a2[1])) ** 2)
    return vectorlen

l = [] #длины отрезков

for i in range(len(a)):
    for j in range(i+1, len(a)):
        l.append(round(vector_len(a[i], a[j]), 2))

# конец части кода, которая ищет все возможные длины отрезков
    
print('Длины всех возможных сторон, при условии что не известен порядок обхода:', l, sep = '\n') 

for i in l:
    if l.count(i) > i:
        print('Это параллелограм')
        break
    else:
        print('Это не параллелограм')
        break

