# Задание-3 (Ферзи):
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске.
# Определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 — координаты 8 ферзей.
# Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

import random


def ferzi():
    n = 8
    x = []
    y = []
    for i in range(n):
        new_x = random.randint(1, 8)   
        new_y = random.randint(1, 8)    
        x.append(new_x)
        y.append(new_y)
    
    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] - x[j] == y[i] -y[j]:
                correct = False
    
    if correct:
        print('NO')
    else:
        print('YES')

if __name__ == "__main__":
    ferzi()