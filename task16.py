# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождения одной строки в другой.

str_1 = input('str_1: ')
str_2 = input('str_2: ')
inkrement = 0
for i in range(len(str_1)):
    if str_2 in str_1[i: i + len(str_2)]:
        inkrement += 1
print(inkrement)
