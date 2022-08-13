def int_func():
    for word in input('Вводите слова через пробел(с маленькой латинской буквы):\n').split():
        bags = 0
        for bag in word:
            if 97 <= ord(bag) <= 122:
                bags += 1
        print(word.title() if bags == len(word) else f'{word} - Только маленькие латинские буквы')

int_func()