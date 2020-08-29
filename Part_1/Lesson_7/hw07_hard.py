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

class PersonNorma:
    def __init__(self, name, surname, cash, rang, norm_hour):
        self.name = name
        self.surname = surname
        self.cash = cash
        self.rang = rang
        self.norm_hour = norm_hour

    @classmethod
    def fract_normalin(cls, str_normalin_worker):
        name, surname, cash, rang, norm_hour = str_normalin_worker.split()
        worker = cls(name, surname, cash, rang, norm_hour)
        return worker

    def __str__(self):
        return(f'{self.name}, {self.cash}, {self.norm_hour}')


class PersonFact:
    def __init__(self, name, surname, worked_hours):
        self.name = name
        self.surname = surname
        self.worked_hours = worked_hours

    @classmethod
    def fract_fact_wh(cls, str_fact_wh):
        name, surname, worked_hours = str_fact_wh.split()
        workes = cls(name, surname, worked_hours)
        return workes

    def __str__(self):
        return(f'{self.name}, {self.worked_hours}')


# class Calculate(PersonNorma, PersonFact):
#     def __init__(self, name, surname, norm_hour, worked_hours, cash):
#         super.__init__(name, surname, norm_hour, worked_hours, cash)

#     def __str__(self):
#         print(f"{self.name}, {self.surname}, {self.norm_hour}, {self.worked_hours}, {self.cash}")


def read_files():
    with open('Part_1\Lesson_7\data\data\workers', 'r+', encoding='utf-8') as file:
        list_norm = file.read().split('\n')
        for i in list_norm[1:]:
            worker1 = PersonNorma.fract_normalin(i)
            print(str(worker1))

    with open('Part_1\Lesson_7\data\data\hours_of', 'r+', encoding='utf-8') as file1:
        list_norm = file1.read().split('\n')
        for i in list_norm[1:]:
            worker2 = PersonFact.fract_fact_wh(i)
            print(str(worker2))
    

if __name__ == "__main__":
    read_files()
