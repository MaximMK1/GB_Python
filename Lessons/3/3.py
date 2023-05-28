# Функции

# def sum(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa  += i
#     return summa
#
# print(sum(15, 'qwert'))
# # Вывод: qwert
#          120


###################

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('M', 'a' 'x', 'i', 'm'))
# print(sum_str('1', '2', '3'))
#
# Вывод: Maxim
#        123

#################

# Рекурсия
# Пользователь вводит число n. Вывести n - первых членов последовательности Фибонначи.
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# list1 = list() # или []
# for i in range (1, 10):
#     list1.append(fib(i))
# print(list1)

########################

# быстрая сортировка (с помощью рекурсии)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array [1:] if i <= pivot]
#     greater = [i for i in array [1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)
#
# print(quick_sort([12,4,3,5,1,2,3,0,6,5,3,7]))

#########################

# сортировка слиянием (с помощью рекурсии)
#
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
#
# list1 = [1,2,4,5,32,2,6,7,0,6,45,4]
# merge_sort(list1)
# print(list1)



