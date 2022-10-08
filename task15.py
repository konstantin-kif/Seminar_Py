# Данно натуральное N, cоздать словарь принимающий значение состоящий из элементов последованности.  
# Пример N = 6 

print({i: 3 * i + 1 for i in range(1, int(input('N: ')) + 1)})

print()

d = {}
for i in range(1, int(input('N: ')) + 1):
    d[i] = 3 * i + 1
print(d)
