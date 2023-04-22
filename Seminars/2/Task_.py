# Вводятся два числа a и b. Найти все простые числа в диапазоне от a до b.

a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        print(i)
