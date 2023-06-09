# def f(x):
#     return x*x
# print(f(5))
#
# a = f
# print((a(5)))

#########################

# def calk1(a, b):
#     return a + b
#
# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calk2, 5, 45)

##########################
# Лямбда функции (сокращенная запись функций)

# def calk2(a, b):
#     return a * b
#
# def math(op, x, y):
#     print(op(x, y))
#
# # def calc1(a, b):
# #     return a + b
#
# # или тоже самое но через лямбда функцию:
#
# # calk1 = lambda a,b: a + b
#
# math(lambda a,b: a + b, 5, 45)

#############################
# Задача:
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# 1 способ

# data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
# res = list()
#
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2)) # i**2 - квадрат числа i
# print(res)

# # 2 способ
#
# def select(f, col):
#     return [f(x) for i in col]
#
# def where(f, col):
#     return [x for x in col if f(x)]
#
# data = [1, 2, 3, 4, 5, 8, 15, 23, 38]
# res = select(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

###################################
# Функция map

# list_1 = [x for x in range(1, 20)]  - генератор списков
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

###########################################

# Задача: C клавиатуры вводится некий набор чисел,
# в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки.
# Как превратить list строк в list чисел?

# data = '15 156 96 3 5 8 52 5'
#
# data = list(map(int, data.split()))
# print(data)

#############################################
#
# # Функция filter
#
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data)) # заполняем список
#                                                 # элементами из начального списка,
#                                                 # которые делятся на 5
# print(res)

#############################################
# Перепишем нашу программу 3 способом, с помощью функций map и filter

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)

############################################

# Функция zip
# Пример:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]
#
# Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

#######################################

# Функция enumerate() позволяет пронумеровать набор данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

# Файлы

# Что нужно для работы с файлами:
# 1. Завести переменную, которая будет связана с этим текстовым файлом.
# 2. Указать путь к файлу.
# 3. Указать, в каком режиме мы будем работать с файлом.

# Варианты режима (мод):
# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
# и в него начнется запись.
# r – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа
# выдаст ошибку.
# w – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует

# 1. w+
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.
# 2. r+
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

# Режим a

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

# Ещё один способ записи данных в файл:
# with open('file.txt', 'w') as data:
# data.write('line 1\n')
# data.write('line 2\n')

# Чтение данных из файла:
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()

# Модуль os
# Модуль os предоставляет множество функций для работы с операционной системой, причем их
# поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою
# программу:
# import os
# Познакомимся с базовыми функциями данного модуля:
# ● os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
# ● os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с
# путями, такие как:
# ○ os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py'))# 'main.py'
# ● os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

# Модуль shutil
# Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок. В частности,
# доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. Часто используется вместе
# с модулем os.
# Для того, чтобы начать работать с данным модулем необходимо его импортировать в свою программу:
# import shutil
# Познакомимся с базовыми функциями данного модуля:
# ● shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
# ● shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# ● shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на
# директорию, а не на символическую ссылку.









