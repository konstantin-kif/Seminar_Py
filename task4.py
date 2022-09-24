# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
#  6,78 -> 7
#  5 -> нет
#  0,34 -> 3

number = float(input("Enter a number: "))
if number - int(number) == 0:
    print("No")
else:
    num = int((number - int(number)) * 10)
    print(num)
