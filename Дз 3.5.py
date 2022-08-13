def sum():
    n = 0
    while True:
        err = False
        list = input('Введите число, введите q чтобы выйти ').split()
        for num in list:
            if num.lower() == 'q':
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    err = True
        if err:
            print('Введенные данные ошибочны!')
        print(f'Сумма чисел = {n}')


print(sum())