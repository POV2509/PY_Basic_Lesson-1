#ДЗ 6.1. Діапазон букв.
#Користувач вводить через дефіс дві літери, Ваше завдання написати програму, яка повертатиме всі символи між ними включно.
#Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#Використовувати модуль string , у якому є string.ascii_letters, з усім набором потрібних букв

import string

input_letters = input("Enter 2 letters with a hyphen (for example a-C): ")

# отримання списку з 2х літер з введенного користувачем
letters = input_letters.split('-')

# друк строки символів string.ascii_letters для наочності
print(string.ascii_letters)
# перевіряємо чи введено 2 літери
if len(letters) == 2 and len(letters[0]) == 1 and len(letters[1]) == 1:
    min_letters = letters[0]
    max_letters = letters[1]
# перевіряємо чи є літери у наборі ascii_letters
    if min_letters in string.ascii_letters and max_letters in string.ascii_letters:
# формуємо результуючий перелік літер (алфавіт англійський) не зважаючі які літери введено
# (за зростанням або за спаданням)
            result_string = ""
            for char in string.ascii_letters:
                if min_letters <= char <= max_letters:
                    result_string += char
                elif max_letters <= char <= min_letters:
                     result_string += char
            print(f"String of letters between {min_letters} and {max_letters} : {result_string}")
    else:
        print("Error. Please,enter 2 English letters")
else:
    print("Error. Please,enter 2 letters with a hyphen (for example a-C): ")


