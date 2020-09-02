# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

fruit = ["яблоко", "банан", "киви", "арбуз"]
n = len(fruit)

for i in range(n):
    print('{}. {:>6}'.format(i+1, fruit[i]))

# Подсказка: воспользоваться методом .format()


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = [1, 'gf', 2.0, 1, 5]
b = ['g', 2.0, 1, 4, 6, 7]

for value1 in b:
    for value2 in a.copy():
        if value1 == value2:
            a.remove(value1)

print(a)
print(b)


# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = [1, 6, 7, 9, 10]
b = []

for i in a:
    if i % 2 == 0:
        b.append(i / 4)
    else:
        b.append(i * 2)
        
print(b)