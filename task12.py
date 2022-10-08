# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_quarter = int(input('Введите номер четверти координатной плоскости: '))

if number_quarter == 1:
    x = 'x > 0' 
    y = 'y > 0'
elif number_quarter == 2:
    x = 'x < 0' 
    y = 'y > 0'
elif number_quarter == 3:
    x = 'x < 0' 
    y = 'y < 0'
elif number_quarter == 4:
    x = 'x > 0' 
    y = 'y < 0'
else:
    print('Такой четверти не сущуствует')
    x = False
    y = False
if bool(x) == bool(y) == True:
    print(f'Диапазон возможных координат точек в этой четверти: {x}, {y}')