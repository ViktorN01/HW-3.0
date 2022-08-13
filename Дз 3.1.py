def my_calc():
    a = int(input('Введите ваше число '))
    b = int(input('Введите ваше число '))
    try:
        res = a // b
    except ZeroDivisionError:
        res = 0
    return res


print(my_calc())
