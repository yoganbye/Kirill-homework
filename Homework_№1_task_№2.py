a = int(input())
b = int(input())
#(a, b) = (b, a) так же проще?!
tmp = a
a = b
b = tmp
print(a, b)