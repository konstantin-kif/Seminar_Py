# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

number = int(input('Enter a number: '))
if number in range(1, 6):
    print('No')
elif number in range(6, 8):
    print('Yes')
