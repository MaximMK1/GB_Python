# Дана строка (возможно, пустая), состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

# Нужно написать функцию RLE,
# которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.

some_str = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
print(some_str)
result_str = ''
count = 1
for i in range(1, len(some_str)):
    if some_str[i - 1] == some_str[i]:
        count += 1
        if i == len(some_str) - 1:
            result_str = result_str + some_str[i] + str(count)
    else:
        result_str = result_str + some_str[i - 1] + str(count)
        count = 1
        if i == len(some_str) - 1:
            print(i)
            result_str = result_str + some_str[i] + str(count)
print(result_str.replace('1', ''))

