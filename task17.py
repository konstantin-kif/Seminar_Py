# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

#print(sum(int(i) for i in input('Введите вещественное число: ') if i.isdigit()))


#num = float(input('N: '))
# while int(num) != num: # вещечтвеное число с запятой не ровна целому
#        num *= 10 # переносим запятую до целого числа

#result = 0
# while num:
#    result += num % 10 #  убирая цифры после десятичной точки.
#    num //= 10 # Выполняет деление и возвращает значение остатка.

# print(result)


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def factorial(input):
#    f = 1
#    for i in range(2, input + 1):
#        f *= i
#    return f
#
#print([factorial(i) for i in range(1, int(input('N: ')) + 1)])

#N = int(input('N: '))

# def fib(N):
#    if N == 1:
#        return N
#    return N * fib(N - 1) # умножить число на одну меньше

#lst = []
# for i in range(1, N + 1):
#    lst.append(fib(i))

# print(lst)

# N = int(input('N: '))

#def fib(N):
#    last = 1
#    for i in range(1, N + 1): # переумножение
#        last *= i
#        yield last

#lst = list(fib(N))
#print(lst)


# Реализуйте алгоритм перемешивания списка.

#import random
#lst = [1,2,3,4,5,6,7,8,9,10]
#random.shuffle(lst)
#lst2 = lst.copy() # копия списка
#lst3 = lst[:] # срез т.е копия списка
#lst2[5] = 98
#print(lst)
#print(lst2)
#print(lst3)

# Задайте список. Напишите программу которая определить, 
# присутствует ли в заданном списке строк некое число.

#lst = ['1', '2fdhf', 'zxc', '2qwe', 'ertqwe']
#N = input('Введите число: ')

#for item in lst:
#    if N in item:
#        print(f'Число {N} найдено в списке, в строке {item}')
#        break

#lst = ['1', '2fdhf', 'zxc', '2qwe', 'ertqwe']
#N = input('Введите число: ')
#for i in lst:
#    if str(N) in i:
#        print('yes')
#        break
#else:
#    print('no N')
    

# Напишите программу которая определить позицию второго вхождении строки
# в списке либо сообщит, что ее нетцук.

lst = ['йцу', 'цук', 'ячс', 'цук', 'йцукен', 'йцу' '12345']
N = input('Введите строку: ')
counter = 0
target_counter = 2

for i in range(len(lst)):
    if N == lst[i]:
        counter += 1
        if counter == target_counter:
             print(f'Строка {N} найдено в списке. Ее {counter} нахождение в списке под индексом {i}')
             break
else:
    print('Сторока не найдена или найдена недостаточно количество раз')
