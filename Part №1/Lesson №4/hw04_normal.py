# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
 
    
    fib1 = 1
    fib2 = 1

    if n == 1 and m > 1:
        print(fib1, fib2, end = ' ')
    if n == 1 and m == 1 or n == 2:
        print(fib2, end = ' ')
    for i in range(2, m):       
        fib1, fib2 = fib2, fib1 + fib2
        if i+1 >= n:
            print(fib2, end = ' ')
        
fibonacci(3, 20)        # что подразумевалось возвращает? вернуть списком или как в примере: "...считать цифры 1 1"
                        # сделал как в примере


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    last_item = len(origin_list) - 1
    for i in range(last_item): #количество элементов в массиве
        for j in range(last_item - i): #cравнение и изменение эл в массиве; -i - уберает сравнение с последним эл
            #print(origin_list)
            if origin_list[j] > origin_list[j+1]:
                origin_list[j], origin_list[j+1] = origin_list[j+1], origin_list[j]
    print(origin_list)

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def filter_craft(func, args):
    var = [i for i in args if func(i) == True]
    return var

n = filter_craft(lambda x: x > 18, [1, 20, 25, 10, 12])
print(n)



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

'''
Данное решение будет True также для трапеции, но если предположить, что трапеция
частный случай параллелограма, как например квадрат или ромб, то всё гуд.
Иное адекватное решение в математике найдено мной не было.....
'''
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

