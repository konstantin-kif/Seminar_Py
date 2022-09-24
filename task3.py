# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:
#  5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number = int(input())
#for value in range(- number, number + 1):
#    print (value, end = ", ")
print(*range(- number, number + 1), sep = ", ")
