# с помощью рекурсии определить является ли слово палиндромом

some_str = input('Введите текст: ')
def polindrom(txt):
    if len(txt) < 2:
        return True
    if txt[0] != txt[-1]:
        return False
    return polindrom(txt[1:-1])

print(polindrom(some_str))

