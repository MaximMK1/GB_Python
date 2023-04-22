# Создайте список из случайных чисел. Найдите номер его последнего
# локального максимума (локальный максимум - это элемент, который больше
# каждого из своих соседей)

listn = list()
import random
for i in range(0, 20):
    listn.append(random.randint(0, 10))
print(listn)
# count = 0
for i in range (1, len(listn)-1):
    count = 0
    if listn[i] > listn[i-1] and listn[i] > listn[i + 1]:
        count += i + 1
        LastMax = count
print(LastMax)