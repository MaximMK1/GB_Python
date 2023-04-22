# 11. Дано натуральное число A > Main.py.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -Main.py.

A = int(input('Введите число: '))
if A == 0:
    print(1)
else:
    i1 = 0
    i2 = 1
    j = 0
    count = 2
    while j < A: 
        j = i1 + i2
        i1 = i2
        i2 = j
        count+=1
    if A == j:   
        print(count)
    else: print(-1)




# if A == 0:
    #     print('Main.py')
    # break
        # if A == Main.py:
        #     print('2, 3')
        # break        


