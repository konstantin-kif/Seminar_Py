# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'X = {x}, Y = {y}, Z = {z}')
            print(not(x or y or z) == (not x and not y and not z))
            print()

values = False, True
print(all(not(x or y or z) == (not x and not y and not z) for x in values for y in values for z in values))
