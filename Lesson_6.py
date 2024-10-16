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


# ДЗ 6.2. Конвертер із числа в дату. Переводить число у формат часу.
#Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.
#Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.
#Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні
# заповнюватися нулями при одноцифрових значеннях (за допомогою методу zfill(2)).
#Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек.
# Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну
# кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)

input_time = int(input("Enter greater than 0 and less than 8640000: "))

# Перевірка чи є число у вказаному діапазоні
if   0 < input_time < 8640000:

# рахуємо кількість днів, годин, хвилин, секунд за допомогою функції divmod (дозволяє обчислити частку
# і залишок від ділення двох чисел у одному виклику)
# отримуємо дні та залишок секунд
    days, seconds = divmod(input_time, 86400)
#print(seconds)
# отримуємо години та залишок секунд
    hours, seconds = divmod(seconds, 3600)
#print(seconds)
# отримуємо хвилини та залишок секунд
    minutes, seconds = divmod(seconds, 60)
#print(seconds)

    day_word = ""
# визначаємо слова для "день" (однина, множина)
    if days == 1 :
        day_word = "day"
    else:
        day_word = "days"
# формування результату конвертації
    formatted_string = f"{days} {day_word},{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
    print(formatted_string)

else:
    print("The number must be between 0 and 8640000")


#ДЗ 6.3. Добуток чисел.
# Перемножити всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
#Користувач вводить число з клавіатури.

input_number = input("Enter a number (integer): ")

# Перевірка чи введено число взагалі
if input_number == "":
    print("Please, enter a number (integer): ")
else:
# Перевірка чи введене ціле число меньше 9, у циклі поки число не є менше 9, премножуємо цифри отриманого числа
    number = int(input_number)
    while number > 9:
        outcome = 1
        for d in str(number):
            outcome *= int(d)
            number = outcome
# друк результату перемножень
    print(f"Result : {number}")
