# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
n = int(input('Введите кол-во элементов: '))
list_a = [random.randint(-10, 10) for _ in range(n)]
X = int(input('Введите число: '))
print(list_a)
# set_a = set(list_a)
diff = abs(list_a[0] - X)
for i in list_a:
    if abs(i - X) < diff:
        diff = abs(i - X)
        number = i
print(number)