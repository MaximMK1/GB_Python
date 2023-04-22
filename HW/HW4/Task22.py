# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input('Введите кол-во элементов первого набора: '))
list_n = [random.randint(-10, 10) for _ in range(n)]
print(list_n)
m = int(input('Введите кол-во элементов второго набора: '))
list_m = [random.randint(-10, 10) for _ in range(m)]
print(list_m)
list_mn = list_n + list_m
set_mn = set(list_mn)
list_mn = list(set_mn)
# print(list_mn)
for i in range(len(list_mn)):
    minIndex = i
    for j in range(i + 1, len(list_mn)):
        if list_mn[j] < list_mn[minIndex]:
            minIndex = j
    temp = list_mn[i]
    list_mn[i] = list_mn[minIndex]
    list_mn[minIndex] = temp
print(f"Упорядоченный список")
print(list_mn)



