# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число N: '))
print(*((-3)**i for i in range(N)), sep=', ')

