# с помощью рекурсии определить является ли число простым или нет


def easy_number(number, divide = 2):
    if number == 1:
        return False
    if number == 2:
        return True
    if number % divide == 0:
        return False
    if divide * divide > number:
        return True
    return easy_number(number, divide + 1)

N = int(input('Введите число: '))
print(easy_number(N))
