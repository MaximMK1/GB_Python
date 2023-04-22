# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

listn = list()
import random
for i in range(0, 6):
    listn.append(random.randint(0, 10))
k = int(input('Input K: '))
print(listn)
listn = listn[k:]+listn[:k]
print(listn)