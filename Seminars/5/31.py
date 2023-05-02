# Задача No31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


# 1 способ
# x = []
# def fibonacci(n):
#     if n in (0, 1):
#         x.append(1)
#         return 1
#     else:
#         r = fibonacci(n-2) + fibonacci(n-1)
#         x.append(r)
#         return r
# n = 7
# fibonacci(n)
# print(x[-(n+1):])

# 2 способ - рекурсия, предложил препод
# n = 0, an = 0     - св-ва ряда Фибонначи
# n = 1, an = 1

# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(6))

# 3 способ, с помощью цикла - оптимальней, тк быстрее работает чем рекурсия

def fib_while(n):
    first = 0
    second = 1
    temp_number = first + second
    count = 2
    while count < n:
        first, second = second, temp_number
        temp_number = first + second
        count += 1
    print(temp_number)

fib_while(6)

# a = 1
# b = 2
# c = 3
# a, c = b, c
#
# print(a, b, c)

