# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

a = 5
data = []

for count in range(0, a):
    data.append(int(input("Input number: ")))

maxl = data[0]
for value in data:
    if value > maxl:
        maxl = value

print("max: ", maxl)
