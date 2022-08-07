def personal(name, surname, year, city, email, phone):
    print(f'name = {name}, surname = {surname}, year = {year}, city = {city}, email = {email}, phone = {phone}')
    return


data = personal(input('Введите ваше имя '), input('Введите фамилию '), input('Введите год рождения '),
                input('Введите город проживания '), input('Введите вашу почту '), input('Введите ваш номер телефона '))
print(data)
