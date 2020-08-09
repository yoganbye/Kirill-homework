# Задание-1:
# Напишите функцию, переводящую км в мили и выводящую информацию на консоль
# т.е функция ничего не возвращает, а выводит на консоль ответ самостоятельно
# Предполагается, что 1км = 1,609 мили
def convert(km):
    miles = km * 1.609
    print(miles)

call = int(input('Введите км: '))

convert(call)

# Задание-2:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
def my_round(number, ndigits):
    integer = int(number) #отделили целую часть    
    fraction = number % 1 * 10 ** ndigits  #отделили остаток    
    balance = float(fraction) - int(fraction) #отделили число после остатка    
    if balance >= 0.5:  #если число после остатка больше 0.5
        return integer + (int(fraction) + 1) / 10 ** ndigits #сложили целую часть и остаток к остатку +1 
    else: #если остаток меньше 0.5
        return integer + int(fraction) / 10 ** ndigits #сложили целую часть и остаток

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

'''
Дробная часть вещественного числа равна остатку от его деления на единицу. 
Целая часть соответственно равна разности самого числа и его дробной части.
Чтобы сохранить определенное количество разрядов после запятой число следует сначала 
сдвинуть влево на соответствующее число разрядов, взять его целую часть и сдвинуть обратно 
в право на столько же разрядов. Сдвиг влево/вправо реализуется умножением/делением на 
основание системы счисления, возведенное в степень равную количеству сдвигаемых разрядов.

Да, это жестко...
'''


# Задание-3:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить, должна возвращать либо True,
# ибо False (если счастливый и несчастливый соответственно)

def lucky_ticket(ticket_number):
    ticket_list = []
    for i in str(ticket_number):
        ticket_list.append(i)    
    sum1 = int(ticket_list[0]) + int(ticket_list[1])
    leng = len(ticket_list)
    sum2 = int(ticket_list[leng-1]) + int(ticket_list[leng-2])
    return sum1 == sum2
        


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
