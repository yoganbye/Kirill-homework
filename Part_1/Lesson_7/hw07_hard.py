# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


# Можно это сделать без использования классов, просто посчитать и записать в файл. 
# Можно сделать это с классами. Класс работник, будет содержать фио, норму часов, зп. 
# И метод который считает зп используя эти атрибуты и количество фактически отработанных часов.
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
    def read_real_hour(surname):
        path2 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'hours_of')
        with open(path2, 'r+', encoding='utf-8') as file1:
            for i, line in enumerate(file1):
                if i > 0 and surname in line:
                    return line

    @classmethod
    def info_to_workers(cls, line):
        name, surname, money, rang, norm_hour = line.split()
        real_hour = Worker.read_real_hour(surname)
        name_j, surname_j, real_hour = real_hour.split()
        footman = cls(name, surname, money, norm_hour, real_hour, rang)   
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
    path1 = os.path.join(os.getcwd(), 'Part_1', 'Lesson_7', 'data\data', 'workers')
    Worker.title()
    with open(path1, 'r+', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i > 0:
                worker1 = Worker.info_to_workers(line)
                worker1.calculation
                worker1.write_file
