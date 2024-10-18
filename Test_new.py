## ДЗ 5.2. Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення -
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
# Виконання 4-х математичних дій (+,-,*,/) з двома операндами ( +виконати перевірку другого операнда -
# при діленні не повинен бути 0.

# # Виконуємо цикл while за умови позитивної відповіді - y
# user_answer = "y"
# while True:
#     user_answer = str(input("Enter 'y' for continue:")).strip().lower()
#     if user_answer != "y":
#         print("Thank you for using the calculator")
#         break
# # введення чисел - визначення зміних (перший та другий операнд)
#
#     number1 = int(input("Enter first number:"))
#     number2 = int(input("Enter second number:"))
# # введення переліку математичних операцій
#     print("\nCalculator")
#     select_math_oper = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
#     print("\nSelect a mathematical operation:")
# #друк математичної операції та її результату в залежності від вибору
#     if select_math_oper == 1:
#         print("Addition")
#         addition = number1 + number2
#         print("Result:",addition)
#     elif select_math_oper == 2:
#         print("Subtraction")
#         subtraction = number1 - number2
#         print("Result:",subtraction)
#     elif select_math_oper == 3:
#         print("Multiplication")
#         multiplication = number1 * number2
#         print("Result:",multiplication)
#     elif select_math_oper == 4:
# #перевірка другого операнду - на 0 ділити не можна
#         if number2 != 0:
#             print("Division")
#             division = number1 / number2
#             print("Result:", division)
#         else:
#             print("You can't divide by 0")
#     else:
#         print("Invalid #ut")
#                        #
#         user_answer = str(input("Enter 'y' for continue:")).strip(#ower()
#         if user_answe#= "y":                                   #
#                 print#("Thank you for using the callator")
#          #  break                           #
##             #



# ДЗ 5.3 Створити hashtag.
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
#
# import string
#
# # Внесення рядка для перетворення у hashtag
# input_string = input("Enter string for hashtag: ")
#
# #перевіряємо на наявність знаків пунктуації та пробілів та видалити їх, створюємо новий рядок
# # та перенаправляємо туди символи строки без пунктуації та пробілів
# cleaned_string = ""
# for char in input_string:
#     if char not in string.punctuation and not char.isspace():
#         cleaned_string += char
# #print(cleaned_string)
# # перевести перші літери слів у великі : спочатку кожне слово рядку перетворює на слово
# # з великої букви, потім розбиваємо рядок на список слів
# input_string = cleaned_string.title().split()
#
# # обєднуємо  список слів в один рядок без роздільників і додаємо # в начало
# hashtag = "".join(input_string)
# hashtag = "#" + hashtag
# # обмежуємо рядок 140 символами
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#
# print(hashtag)


# ДЗ 7.2. Модифікувати рядок.
# На вхід функції correct_sentence передається два речення. Необхідно повернути їх виправлену копію так,
# щоб вони завжди починалися з великої літери та закінчувалися крапкою.Якщо речення вже закінчується крапкою,
# додавати ще одну не потрібно, це буде помилкою.
# Вхідні, вихідні аргументи: string.

# Функція з двома аргументами (str), для перетворення у два речення з великої,з точкою (одною) у кінці.
def correct_sentence(sent1: str, sent2: str) -> str:
# функція для коректування речення: перша буква на велику та одна крапка у кінці
        def correct_sent(sent: str) -> str:
            sent = sent.strip(",").capitalize()
# перевірка\додавання крапки у кінці
            if  not sent.endswith("."):
                sent += "."
            return sent
# коректуємо обидва речення
        corrected_sent1 = correct_sent(sent1)
        corrected_sent2 = correct_sent(sent2)

# повертаємо відкоректовані речення
        return f"{corrected_sent1} {corrected_sent2}"

# Використання
print(correct_sentence("glad to see you","Have a nice day everyone"))
print(correct_sentence("dear society.","have a safe day."))



