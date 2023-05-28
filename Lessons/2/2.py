# Коллекции данных

# Списки

list_1 = [] 
list_1 = list()
list_1 = [1,2,3,8]
print(list_1)
print(*list_1)

for i in list_1:
    print(i)

print(len(list_1))

print(list_1[0])
print(list_1[1])
print(list_1[-1])
print(list_1[3])

list_1 = [1, 5]
print(list_1)
list_1.append(8)  # добавление в список элемента со значением "8" (в конец списка)

list = []
for i in range(5):
    list.append(i)
    print(list)

# Функции в списках

# Удаление последнего элемента списка
list = [12, 5, 6, 7, 34]
print(list.pop())   # удаляется последний элемент списка "34"
print(list) # [12, 5, 6, 7]

a = list.pop() # функция pop удаляет последний элемент списка
print(a) # 34, и возвращает его

# удаление конкретного элемента списка
list_1 =[12, 6, -1, 21, 0]
print(list_1.pop(0)) # удаление нулевого элемента списка "12"
print(list_1) # [6, -1, 21, 0]

# добавление элемента на нужную позицию
list_1 = [12, 7, -1, 21, 0]
print(list_1.insert(2, 11))
print(list_1) # [12, 7, 11, -1, 21, 0]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0]) # 1
print(list_1[1]) # 2
print(list_1[-1]) # 10
print(list_1[-5]) # 6
print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2]) # [1, 2]
print(list_1[len(list_1)-2:]) # [9, 10]
print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list_1[6:-18]) # []
print(list_1[0:len(list_1):6]) # [1, 7]
print(list_1[::6]) # [1, 7]

# задача 
# Создать список, состоящий из четных чисел в диапазоне от 1 до 100
# вариант 1
list_1 = []
for i in range (1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,...,100] - все числа от 1 до 100
# вариант 2
list_1 = [i for i in range(1, 101) if i % 2 == 0]   # только четные
print(list_1)  # [2, 4, 6,...,100]



# кортежи
t = (1, 5, 4,) # кортеж отличается от списка тем,
               # что он в круглых скобках и после последнего элемента есть запятая

v = [1, 8, 9] # создание списка
print(v)
print(type(v))

v = tuple(v) # преобразование списка в кортеж (tuple - кортеж)
print(v)
print(type(v))

a, b, c = v

print(a, b, c) # 1 8 9  - переменным a, b, c присвоились значения элементов кортежа
               # распаковка кортежа

# a = 1
# b = 2   или   a, b = 1, 2  присваивание значений переменным

t = (1, 2, 3, 5, )
print(t[1]) # 2

for i in t:
    print(i)

for i in range (len(t)):
    print(t(i))

# Словари
d = {}
d = dict()

d['q'] = 'qwerty'
print(d) # {'q': 'qwerty'}

d['w'] = 'werty'
print(d) # {'q': 'qwerty', 'w': 'werty'}
print(d['q']) # qwerty

# пример
dictionary = {}
dictionary = {'up': '|', 'left': '<'}
print (dictionary) # {'up': '|', 'left': '<'}
print (dictionary['left']) # <
print (dictionary['up']) # |

del dictionary['left'] # удаление элемента из словаря

for item in dictionary:  # item - ключ
    print(item) # up
                # up left
    print ('{}:{}'.format (item, dictionary[item])) # up: |
                                                    # left: <

for (k, v) in dictionary.items():
    print(k, v)                   # up: |
                                  # left: <  
                        
# множества
colors = {'red', "green", 'blue'}
print(colors) # {'red', "green", 'blue'}
colors.add('red')
print(colors) # {'red', "green", 'blue'}
colors.add('gray')
print(colors) # {'red', "green", 'gray', 'blue'}
colors.remove('red')
print(colors) # {"green", 'gray', 'blue'}
colors.discard('red') # ok    функция discard проверяет есть ли во множестве
                      # элемент со значением red, если да то он удаляется, если нет 
                      # то ничего не делает
colors.clear() # { }  очистка множества
print(colors) # set() set - пустое множество

q = set() # - создание пустого множества

# операции со множествами
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21} # объединение множеств
i = a.intersection(b) # i = {8, 2, 5} # пересечение множеств
dl = a.difference(b) # dl = {1, 3} # разница множеств
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # q = {1, 21, 3, 13} 

# пример
a = {1, 8, 6}
b = frozenset(a)  # заморозка множества(нельзя изменить)
print(b) # frozenset({1, 8, 6})





                