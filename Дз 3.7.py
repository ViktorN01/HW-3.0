def func(word):
    latin_letter = 'qwertyuiopasdfghjklzxcvbnm'
    return word.title() if not set(word).difference(latin_letter) else False


words = input('Введите строку из слов, разделенных пробелом: ').split()
for i in words:
    result = func(i)
    if result:
        print(result, ' ')