# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# +1. Получить полный список всех классов школы
# +2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# +4. Узнать ФИО родителей указанного ученика
# +5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, name:str, surname:str, patronymic:str):
            self._name = name
            self._surname = surname  
            self._patronymic = patronymic   

    def get_short_name(self):
        return f'{self._surname} {self._name[0]}.{self._patronymic[0]}.'

    def get_fullname(self):
        full_name = self._surname + " " + self._name + " " + self._patronymic
        return full_name

class Class_room:
    def __init__(self, class_number, subjects, teachers):
        self._class_number = class_number
        self._subjects = {subjects: teachers}
        self._teachers = teachers

    def get_class_number(self):
        return self._class_number

    def get_teachers(self):
        return self._teachers

class Teacher(Person, Class_room):
    def __init__(self, name, surname, patronymic, subject):
        super().__init__(name, surname, patronymic)            
        self._subject = subject

class Student(Person, Class_room):
    def __init__(self, name, surname, patronymic, class_number:str, mother:str, father:str):
        super().__init__(name, surname, patronymic)   
        self._class_number = class_number
        self._mother = mother
        self._father = father
    
    def parents(self):
        return f'Mother: {self._mother}, Father: {self._father}'        
    
        
        
classes = [Class_room("5A", "Математика", "Карпов Анатолий Михайлович"),
           Class_room("6A", "Физика", "Бондарева Мила Степановна")]
 
teachers = [Teacher("Анатолий", "Карпов", "Михайлович", "Математика"),
            Teacher("Сан", "Кириллов", "Саныч", "Физкультура"),
            Teacher("Мила", "Бондарева", "Степановна", "Физика"),
            Teacher("Мария", "Чижикова", "Анатольевна", "Химия")]
 
students = [Student("Андрейцев", "Илья", "Андреевич", "6A", "Анна", "Андрей"),
            Student("Булкин", "Пирожок", "Маркович", "5A", "Хлеб", "Масло"),
            Student("Марков", "Дмитрий", "Андреевич", "5A", "Евгения", "Андрей"),
            Student("Александр", "Сергеевич", "Пушкин", "6A", "Надежда", "Сергей")]

def get_all_class_on_school():
    #Принтит все классы школы
    print("Все классы школы: ")
    for i in classes:
        print(i.get_class_number())
    print()
   

def get_all_studients():
    #Имена учеников в каждом классе
    for j in classes:
        a = j.get_class_number()
        print(f"Ученики в классе {a}: ")               
        for i in students:
            b = i.get_class_number()
            if b == a:
                print(i.get_short_name())
        print() 
                
def parents_students():
    #Имена родителей
    for i in students:
        print("Родители ", i.get_short_name())
        print(i.parents())
        print()

def get_all_teacher():
    #Список учителей преподающих в классе
    for j in classes:
        a = j.get_teachers() 
        c = j.get_class_number()
        print(f"Учителя преподающие в классе {c}: ")         
        for i in teachers:                           
            b = i.get_fullname() 
            if b in a:
                print(j.get_teachers())      
        print()   
    
get_all_class_on_school()
get_all_studients()
parents_students()
get_all_teacher()
