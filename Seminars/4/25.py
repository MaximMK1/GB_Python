# 25. Напишите программу,
# которая принимает на вход строку,
# и выводит кол-во повторов
# каждого из символов 1 раз.

1 способ
some_str = '4678t435g7wy347832f'
count_dict = {} # a: 3
for letter in some_str:
    if letter not in count_dict:  # если елемент не встречается в словаре(в ключе)
        count_dict[letter] = 1 # то создаем в словаре ключ со значением 1
    else:
        count_dict[letter] = count_dict[letter] + 1 # иначе прибавляем к значению этого ключа еще раз 1
print(count_dict)

# # 2 способ
# some_str = input()
# for i in set(some_str):
#     print(i, some_str.count(i))

# 3 способ
# some_str = input()
# for letter in set(some_str):
#     count = 0
#     for letter1 in (some_str):
#         if letter == letter1:
#             count += 1
#     print(letter, count)







