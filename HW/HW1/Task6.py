# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = int(input("Введите шестизначное число: "))

count = 0
temp = n
while temp > 0:
    count += 1
    temp = temp // 10

if count != 6:
    print("Вы ввели не шестизначное число")
else:
    summa1 = 0
    while n > 999:
        x = n % 10
        summa1 += x
        n //= 10
   
    summa2 = 0
    while n > 0:
        x = n % 10
        summa2 += x
        n //= 10
   
    if (summa1 == summa2):
        print("Билет счастливый")
    else:
        print("Билет несчастный(")
