def my_func(a, b, c):
    try:
        if a >= b and a > c and b > c or b >= a and a > c and b > c:
            sum = a + b
            print(sum)
        elif a > b and a >= c and c > b or c >= a and c > b and a > b:
            sum = a + c
            print(sum)
        elif c > a and b > a and b >= c or c > a and b > a and c >= b:
            sum = b + c
            print(sum)
        else:
            print('err')
    except:
        sum = 0
        return sum


sum1 = my_func(int(input('enter your a:')), int(input('enter your b:')), int(input('enter your c:')))
print(sum1)
