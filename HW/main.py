def test(x):
    return lambda n: n % x == 0

func = test(2)
print(func(8))