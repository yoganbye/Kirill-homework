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
    len_face = len(ticket_list) // 2

    sum1 = 0
    sum2 = 0
    count = 0
    while count < len_face:
        sum1 += int(ticket_list[count])        
        count +=1     
        sum2 += int(ticket_list[-count]) 
    
    return sum1 == sum2
  

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))

