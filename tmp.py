
a = '41242111143443333223233545444544222232'

tmp = ''
maximum = ''
for i in range(len(a) - 1):
    if len(tmp) == 0 and (a[i] == a[i+1] or a[i] == a[i-1]):
        tmp += a[i]
    elif (a[i] == a[i+1] or a[i] == a[i-1]) and a[i] in tmp:
        tmp += a[i]
    elif len(tmp) > len(maximum):
        maximum = tmp
        tmp = ''
    else:
        tmp = ''
    
print(maximum)
