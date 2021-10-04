import HomeWork15
import re


firstname = input('Введите Фамилию: ')
secondename = input('Введите Имя: ')

validated = 0
while validated == 0:
    try:
        phn = input('Введите Номер телефона в формате 0670000000: ')
        pattern = r'^\d{10}$'
        if not re.match(pattern, phn):
            raise Exception("Номер введен в некоректном формате формат номера 0670000000")
        validated = 1
    except Exception as e:
        print(e)
        validated = 0

HomeWork15.insert_new_phone(firstname, secondename, phn)
print('Success')
HomeWork15.print_all_phones()

