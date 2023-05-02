# Задача 18: Требуется найти в массиве A самый близкий по величине элемент
# к заданному числу X. Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел
# Ai (можно использовать псевдогенерацию). Последняя строка содержит число X

# *Пример:*

# 5
#     7 -2 3 5 1
#     6
#     -> 7

import random
n = int(input('Введите размер массива: '))
a = [random.randint(1, 10) for i in range(n)]
print(a)
x = int(input('Введите число: '))
a = set(a)
var = 0

if x < min(a):
    print(min(a))

elif x > max(a):
    print(max(a))

else:
    while True:
        if x - var in a and x + var in a and x - var != x + var:
            print(x - var, x + var)
            break

        elif x - var in a:
            print(x - var)
            break

        elif x + var in a:
            print(x + var)
            break

        else:
            var += 1
