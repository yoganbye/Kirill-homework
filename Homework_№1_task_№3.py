import math
a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - 4 * a * c
d = math.sqrt(D)
x1 = (- b + d) / 2 * a
x2 = (-b - d) / 2 * a
#print('x1 = ' + str(x1) + '\n' + 'x2 = ' + str(x2))
print(x1)