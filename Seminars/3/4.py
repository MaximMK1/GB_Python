# Задача 23.
# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)

listn = list()
import random
for i in range(0, 8):
    listn.append(random.randint(0, 10))
print(listn)
count = 0
# print(len(listn))
# print(listn[0])
for i in range(len(listn) -1):
    if listn[i] < listn[i+1]:
        count += 1
print(count)



