# Задача 17. Дан список чисел. Определите,
# сколько в нем встречается различных чисел.

listn = list()
count = 0
while True:
    n = int(input("Input num: "))
    listn.append(n)
    if listn.count(n) == 1:
        count += 1
    print(count)
    print(listn)

# # 2 способ
# listn = [1, -1, 2, 0, 1, 3, 4, 4, 4, 8]
# num = set(listn)
# print(num, len(num))
