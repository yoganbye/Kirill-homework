# Не обращать внимание!! Чисто черновик
a = [1, 6, 7, 9, 10]
b = []

for i in a:
    if i % 2 ==0:
        b.append(i / 4)
    else:
        b.append(i * 2)
        
print(b)