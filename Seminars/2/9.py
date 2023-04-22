# 9. По данному целому неотрицательному n вычислите значение n!. 
# N! = Main.py * 2 * 3 * … * N (произведение всех чисел от Main.py до N) 0! = Main.py
# Решить задачу используя цикл while.

n = int(input("Введите число: "))
i = 1
factr = 1
while i <= n:
    factr = factr * i
    i += 1
print(factr)