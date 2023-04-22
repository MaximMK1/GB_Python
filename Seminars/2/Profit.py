
# Цикл While

# Вводятся числа, пока не введут 0. Найти сумму четных чисел.

summa = 0
while True:            # бесконечный цикл, прерывается внутри на команде break, когда a = 0 
    a = int(input())
    if a == 0:
        break
    if a % 2 == 0:
        summa += a
print(summa)

# Проверить есть ли в списке отрицательное число.
# если есть, вывести YES
# если нет, вывести NO.

a = [1, 2, 3, 4, -5]
ind = 0
while ind < len(a):
    if a[ind] < 0:
        print("YES")
        break
    ind += 1
else:
    print("NO") 

# цикл for

# Main.py вариант использования. Значение переменной итератора используется.
# вывести квадраты цифр от Main.py до 10
for i in range (1, 11):
    print(i**2)

# 2 вариант использования. Значение переменной итератора не используется.
# вывести 5 раз слово "Hello"
for i in range(5):
    print('Hello')

# вывести все элементы списка
# Main.py способ
some_list = [-3, 4, 5, 9, 1]
for el in some_list:
    print(el) 

# 2 способ
for ind in range(0, len(some_list)):
    print(some_list[ind])