# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

stringer = input('Введите выражение, после ввода Enter: ') #Вводить следует корректно, пограничные 
                                                           #условия не учтены, код и так душный вышел
from fractions import Fraction
#Начало части кода, которая разделяет операнды по отдельным спискам, деля дробную и целую часть
#stringer = '-1 5/6 + -2/7'
sym = stringer.split(' ')
a = []
for i in range(2): #двойка - количество вложенных списков, можно было как то иначе оформить, но в условии
       b = []      #указано что операции будут проводиться для двух операндов
       if len(a) == 0: #первое вхождение до знака плюс или минус
              for j in sym:
                     if j == '+' or j == '-':
                            break
                     else:
                            b.append(j)
       
       else:         #второе вхождение после знака плюс или минус
              for j in range(len(a[0]), len(sym)):
                     if sym[j] != '+' and sym[j] != '-':
                            b.append(sym[j])     

       a.append(b)       

#print(a)
#Конец части кода, которая разделяет операнды по отдельным спискам, деля дробную и целую часть

#начало кода, суммы целых и дробных частей операндов
sym1 = 0
if a[0][0][:1] == '-':
       for i in a[0]:
              sym1 -= abs(Fraction(i))
else:
       for i in a[0]:
              sym1 += Fraction(i)         

#print(sym1)

sym2 = 0
if a[1][0][:1] == '-':
       for i in a[1]:
              sym2 -= abs(Fraction(i))
else:
       for i in a[1]:
              sym2 += Fraction(i)        

#print(sym2)
#конец кода, суммы целых и дробных частей операндов; т.к. количество операндов известно, то функцию не реализовываю

#Начало кода вычесление суммы операндов в дробном эквиваленте
if '+' in sym:
       ultra_sum = Fraction(sym1) + Fraction(sym2)
else:
       ultra_sum = Fraction(sym1) - Fraction(sym2)

print(ultra_sum)
#Конец кода кода вычесление суммы операндов в дробном эквиваленте

#Начало кода, вычленение целой части из ответа

arg = str(ultra_sum).split('/')
whole = abs(int(arg[0])) // int(arg[1])

if float(ultra_sum) < 0:           #Баг или фича, не понял...
       fraction = int(arg[0]) % int(arg[1]) + 1
else:
       fraction = int(arg[0]) % int(arg[1])

if abs(int(arg[0])) > int(arg[1]):
       if '-' in arg[0]:
              print(f'-{whole} {fraction}/{arg[1]}')
       else:
              print(f'{whole} {fraction}/{arg[1]}')
else:
       print(ultra_sum)

'''
Бывает выдает ошибку, для того чтобы сработал код, необходимо повторно его включить
'''

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
import os


class Worker:
    def __init__(self, name, surname, money, norm_hour, real_hour, rang):
        self.name = name
        self.surname = surname
        self.money = int(money)
        self.norm_hour = int(norm_hour)
        self.real_hour = int(real_hour)
        self.rang = rang

    @staticmethod
    def read_file():
        path1 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'workers')
        path2 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'hours_of')

        with open(path1, 'r+', encoding='utf-8') as file:
            list_norm = file.read().split('\n')

        with open(path2, 'r+', encoding='utf-8') as file1:
            list_real = file1.read().split('\n')
        return list_norm, list_real

    @classmethod
    def info_to_worker(cls):
        list_norm, list_real = Worker.read_file()
        Worker.title()
        for i in list_norm[1:]:
            name, surname, money, rang, norm_hour = i.split()
            for j in list_real[1:]:
                name_j, surname_j, real_hour = j.split()
                if surname == surname_j:
                    footman = cls(name, surname, money, norm_hour, real_hour, rang)
                    footman.calculation
                    footman.write_file
        return footman   

    @property
    def calculation(self):
        if self.norm_hour > self.real_hour:
            result_money = self.money / self.norm_hour * self.real_hour
        else:
            result_money = self.money + (self.money / self.norm_hour * self.real_hour - self.norm_hour) * 2
        self.result_money = round(result_money)
        return self.result_money

    @property
    def write_file(self):
        with open('data_worker_of_price.txt', 'a+', encoding='utf-8') as out:
            out.write('{}{}{}{}\n'.format(self.name.ljust(15), self.surname.ljust(15),\
                                         self.rang.ljust(20), self.result_money))

    @staticmethod
    def title():
        with open('data_worker_of_price.txt', 'a+', encoding='utf-8') as out:                
            out.write('{}{}{}{}\n'.format('Имя'.ljust(15), 'Фамилия'.ljust(15),\
                                        'Должность'.ljust(20), 'Зарплата к выдаче'))



if __name__ == "__main__":
    worker1 = Worker.info_to_worker()






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

dikt_fruts = dict()

path = os.path.join(os.getcwd(), 'Part_1', 'Lesson_4', 'data', 'fruits.txt')
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
