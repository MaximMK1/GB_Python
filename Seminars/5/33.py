# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
def replacement (some_list):
    min_item = min(some_list)
    max_item = max(some_list)
    for i in range(len(some_list)):
        if some_list[i] == max_item:
            some_list[i] = min_item
    return some_list

some_list = [random.randint(1, 6) for _ in range(5)]

print(some_list)
print(replacement(some_list))
