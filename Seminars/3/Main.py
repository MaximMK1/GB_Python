# как пройти по индексам строки

# some_str = 'hello'
# for letter in some_str:
#     print(letter)
#
# for ind in range(0, len(some_str)):
#     print(some_str[ind])
#
# print(some_str[-2])
#
# print(some_str[1:4:2])  # срез строки, выводят символы с 1 по 4 с шагом 2
# print(some_str[::-1])  # перевернуть строчку
#
# # списки
#
# some_list = [1, 'fds', True, [1, 2, 3], {1: 2}, (5, 7)] # список может состоять из разных типов данных
# print(some_list)
# print(some_list[1])
#
# some_list = []    # Заполнение пустого списка, введенными значениями (10 элементов)
# for _ in range(10):
#     number = int(input())
#     some_list.append(number)
# print(some_list)
#
# some_list = [int(input()) for _ in range(10)] # тоже самое но в одну строчку

# import random
# some_list = []    # Заполнение пустого списка, рандомными значениями от 1 до 10
# for _ in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)

# import random
# some_list = []
# for _ in range(10):
#     number = random.randint(1, 10)
#     some_list.append(number)
# print(some_list)
# print(some_list.count(7)) # проверяет сколько цифр 7 в списке
# print (7 in some_list) # проверяет есть ли цифра 7 в списке (True/False)
#
# # поменять значения местами у переменных
# a = 10
# b = 5
# a, b = b, a
# print(a, b)

# кортеж
# a = [1, 2, 3]
# b = tuple(a) # кортеж
# for i in b:
#     print(i)
# print(b[0])
#
# a = (1, )

# множества
# a = set()
# for i in range(1, 10):
#     a.add(i)
# print(a)
#
# a = {1, 2, 3}
# print(type(a))

# import random      # замерить время работы того или алгоритма. И сравнить их время работы
# import time
# some_list = [random.randint(1, 10000) for i in range(10 ** 7)]
# some_set = set(some_list)
#
# start = time.perf_counter()
# print(11000 in some_list)
# end = time.perf_counter()
# duration1 = end - start
#
# start = time.perf_counter()
# print(11000 in some_set)
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration1 / duration2)

# a = frozenset()

# словари

# some_dict = {яблоко: 'apple', апельсин: 'orange'}
# print(some_dict['яблоко'])     #
# print(some_dict.get('груша'))  # вывод значения по ключу
# print(some_dict['груша'])      #

# some_dict['виноград'] = 'grape'
# print(some_dict)

# # неизменяемые типы данных
# str, int, float,  bool, tuple, frozenset,
#
# # изменяемые
# list, set, dict

# из двух списков сделать словарь
# a = [1, 2, 3]
# b = ['1', '2', '3']
# c = {}
# for ind in range (0, len(a))
#     c[a[ind]] = b[ind]
# print(c)









