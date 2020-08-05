# Предметная область – университет. Разработать класс University, описывающий работы
# университета. Разработать класс People, описывающий человека, человек характеризуется 
# параметрами: фамилия, имя, отчество, дата рождения, телефон. Разработать класс Students на 
# базе класса People, студент описывается следующими параметрами: уникальный идентификатор студента,
# ФИО студента, номер группы, признак старосты группы, код специальности.



class University:
    pass

class People:
    def __init__(self, name, surname, patronymic, born_day, num_tel):
        self._name = surname
        self._surname = surname
        self._patronymic = patronymic
        self._born_day = born_day
        self._num_tel = num_tel    

    @property
    def get_info(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}\nОтчество: {self._patronymic}\
                \nДень рождения: {self._born_day}\nНомер телефона: {self._num_tel}"

    def set_name(self, name):
        self._name = name
        return(f'Имя изменено на {self._name}')

    def set_surname(self, surname):
        self._surname = surname
        return(f'Фамилия изменена на {self._surname}')

    def set_patronymic(self, patronymic):
        self._patronymic = patronymic
        return(f'Отчество изменено на {self._patronymic}')

    def set_num_tel(self, num_tel):
        self._num_tel = num_tel
        return(f'Номер телефона изменен на {self._num_tel}')


class Student(People):
    def __init__(self, name, surname, patronymic, born_day, num_tel, id_code, num_groupe, 
                praepostor, num_special):
        super().__init__(name, surname, patronymic, born_day, num_tel)
        self._id_code = id_code
        self._num_groupe = num_groupe
        self._praepostor = praepostor
        self._num_special = num_special

    def set_id_code(self, id_code):
        self._id_code = id_code
        return(f'Идентификатор студента изменен на {self._id_code}')

    def set_num_groupe(self, num_groupe):
        self._num_groupe = num_groupe
        return(f'Номер группы изменен на {self._num_groupe}')

    def set_praepostor(self, praepostor):
        self._praepostor = praepostor
        return(f'Назначен/снят старостой {self._praepostor}')    

    @property
    def get_info(self):
        return f"Имя: {self._name}\nФамилия: {self._surname}\nОтчество: {self._patronymic}\
                \nДень рождения: {self._born_day}\nНомер телефона: {self._num_tel}\
                \nИднетификатор студента: {self._id_code}\nНомер группы: {self._num_groupe}\
                \nСтароста: {self._praepostor}\nНомер специальности: {self._num_special}"
