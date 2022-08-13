#comp = lambda x, y: x ** y
#print(comp(10, -3))

def func(x, y):
    x, y =float(x), int(y)
    if x >= 0 and y < 0:
        res = 1
        for n in range(y):
            res *= 1
            print(func(2, -3))
    else:
        print('err')
    return func(x, y)

print(func(10, -2))






