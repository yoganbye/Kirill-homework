# Предметная область - предприятие. Разработать класс Enterprise, описывающий работу с предприятием.
# Разработать класс People, описывающий человека, человек характеризуется параметрами:
# фамилия, имя, отчество, дата рождения, телефон. Разработать класс Employees на базе
# класса People, сотрудник характеризуется следующими параметрами: уникальный
# идентификатор сотрудника, код отдела, заработная плата.

from abc import ABC, abstractmethod

class EnterpriseFactory(ABC):
    @abstractmethod
    def assign_work(self, name):
        pass


class Enterprise(EnterpriseFactory):
    count_work = 0

    def __init__(self, name):
        self._name = name

    def assign_work(self):
        if Enterprise.count_work > 0:
            return (f'{self._name} уже выполняет работу')
        else:
            Enterprise.count_work += 1
            self._work = input(f'{self._name} нигде не работает. Назначте работу: ')
            return (f'Вы отправили работягу {self._name} {self._work}')

    def info_work(self):
        return(f'{self._name} работает {self._work}')


class People(Enterprise):
    def __init__(self, name, surname, patronymic, born_day, num_tel):
        super().__init__(name)
        self._surname = surname
        self._patronymic = patronymic
        self._born_day = born_day
        self._num_tel = num_tel
    
    def set_people(self, name, surname, patronymic, born_day, num_tel):
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._born_day = born_day
        self._num_tel = num_tel

    @property
    def get_info(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}\nОтчество: {self._patronymic}\
                \nДень рождения: {self._born_day}\nНомер телефона: {self._num_tel}"

   
class Employees(People):
    def __init__(self, name, surname, patronymic, born_day, num_tel, id_code, code_deport, wage):
        super().__init__(name, surname, patronymic, born_day, num_tel)
        self._id_code = id_code
        self._code_deport = code_deport
        self._wage = wage

    @property
    def get_info(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}\nОтчество: {self._patronymic}\
                \nДень рождения: {self._born_day}\nНомер телефона: {self._num_tel}\
                \nЛичный идентификатор:{self._id_code}\nНомер депортамента: {self._code_deport}\
                \nЗаработная плата: {self._wage}"

    def set_employ(self, id_code, code_deport, wage):
        self._id_code = id_code
        self._code_deport = code_deport
        self._wage = wage  

  

footman = Employees('Валерий', 'Жмышенко', "Альбертович", "01.14.88", '8(343)22-81-488', '88_14', 
                 '14_228', '10$')

print(footman.get_info)
print()
print(footman.assign_work())
print()
print(footman.info_work())
print()
print(footman.assign_work())
