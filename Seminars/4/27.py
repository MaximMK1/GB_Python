# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


# 1 способ
# text = '111 1 1 1  ,   2 2 2 3 3 4      '
# word = ''
# list = set()
# for i in text:
#     if i != ' ':
#         word += i
#     else:
#         if word != '':
#             list.add(word)
#         word = ''
# print(list)
# print(len(list))


# 2 способ (мой)
# text = '1 she sells 2 2 2 1 1 sea shells on the sea shore rhgbjh nsdjkfn rhgbjh 1 1 1 1 1 1'
# word = ''
# list = set()
# for i in range(len(text)):
#     word = word + text[i]
#     if text[i] == " ":
#         list.add(word)
#         word = ''
#     if i == (len(text)-1):
#         list.add(word + ' ')
# list.discard(' ')
# print(list)
# print(len(list))

# 3 способ
# text = '1 she rhgbjh nsdjkfn rhgbjhr' + ' '
# count = 0
# list = set()
# for i in range(len(text)):
#     if text[i] == ' ':
#         list.add(text[count: i]) # добавляем во множество list часть строки text от элемента count до i не включительно
#         count = i + 1
# print(list)
# print(len(list))

# 4 способ
# some_str = input().split() # метод split разделяет строку на слова по пробелу, на выходе получаем список
#                            # можно и по другому разделителю (не по пробелу)
# print(some_str)
# print(len(set(some_str)))

# # 5 способ
# some_str = input()
# some_str = some_str.replace(',', ' ')
# some_str = set(some_str.split())
# print(some_str)
# print(len(some_str))


