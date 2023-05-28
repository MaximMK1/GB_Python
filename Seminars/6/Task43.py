# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:        Вывод:
# 1 2 3 2 3      2

# # мой способ
#
import random
list1 = [random.randint(0, 10) for i in range(28)]
# list1 = [6, 10, 9, 3, 0, 3, 3, 9, 8, 6]
print(list1)
list1.sort()
print(list1)
temp_list = list()
count = 1
for i in range(1, len(list1)):
    # print(i)
    if list1[i - 1] == list1[i]:
            count += 1
            if i == len(list1) - 1:
                temp_list.append(count)
                # print(count)
    else:
        temp_list.append(count)
        if i == len(list1) - 1:
            count = 1
            temp_list.append(count)
            # print(count)
        count = 1
# print(temp_list)
sum = 0
for i in temp_list:
    q = i // 2
    # print(q)
    sum = sum + q
print(sum)

# способ преподавателя

list_1 = [1, 2, 3, 2, 3]
count = 0
for i in range(len(list_1)):
    for j in range(i + 1, len(list_1)):
        if i != j and list_1[i] == list_1[j]:
            count += 1
print(count)



