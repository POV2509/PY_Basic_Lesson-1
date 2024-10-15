# ДЗ 5.1  Ім`я змінної. Ціль - перевірка чи може довільний рядок бути іменем змінної
# Змінна не може: починатися з цифри , містити великі літери, пробіл і знаки пунктуації,
# окрім нижнього підкреслення "_", бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# пробіл і знаки пунктуації можна взяти з string.punctuation;
# cписок зареєстрованих слів можна взяти із keyword.kwlist.

# завантажимо модуль string, буде використовуватись для перевірки на наявність пробілов
# та знаків пунктуації
import string
# завантажимо модуль keyword, буде використовуватись для перевірки на наявність зареєстрованих слів
import keyword
# створимо тестовий перелік варіантів імен змінних
variable_names_for_check = ["_", "__", "sum", "x", "get_value", "get value", "get!value", "some_super_puper_value",
                         "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert__exception"]
#variable_names_for_check = ["some_super_puper_value"]


for name_for_check in variable_names_for_check:
# перевіряємо чи є хоч один символ у імені змінної, шоб мало сенс подальші перевірки
    if len(name_for_check) > 0 :
# перевіряємо чи є один символ "_" у імені змінної (виключення)
        if name_for_check[0] == "_" and len(name_for_check) == 1:
            print(f"Variable name '{name_for_check}' is correct!")
#перевіряємо на зареєстровані слова (keyword.kwlist)
        elif name_for_check in keyword.kwlist:
                print(f"Variable name '{name_for_check}' is in the keyword (reserved keyword)!")
        else:
# перевіряємо шоб змінна не починалась з цифри,  взагалі не містила  великих букв та пробілів
                if not name_for_check[0].isdigit() and name_for_check.islower() and not name_for_check.count(" ") != 0:
                    for s in string.punctuation.replace("_", ""):
                        if s in name_for_check:
                            print(f"Found '{s}'. Variable name '{name_for_check}' is not correct! ")
                            break
#  перевіряємо чи є підряд підкреслення:
                        elif "_" in name_for_check:
                            for i in range(len(name_for_check) - 1):
                                    if name_for_check[i] == "_" and name_for_check[i + 1] == "_":
                                        print(f"Variable name '{name_for_check}' is not correct! has several underscores in a row!")
                                    break
                        print(f"Variable name '{name_for_check}' is correct!")
                        break
                else:
                    print(f"Variable name '{name_for_check}' is not correct!")
    else:
        print(f"Variable length '{name_for_check}' is not correct!")


# ДЗ 5.2. Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче.
# Тобто, потрібно робити запит до користувача на продовження роботи калькулятора після кожного обчислення
# якщо користувач ввів yes (можна просто y), то нове обчислення, інакше - закінчення роботи.
# Виконання 4-х математичних дій (+,-,*,/) з двома операндами ( +виконати перевірку другого операнда -
# при діленні не повинен бути 0.

# Виконуємо цикл while за умови позитивної відповіді - y
user_answer = "y"
while True:
    user_answer = str(input("Enter 'y' for continue:")).strip().lower()
    if user_answer != "y":
        print("Thank you for using the calculator")
        break
    # введення чисел - визначення зміних (перший та другий операнд)

    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    # введення переліку математичних операцій
    print("\nCalculator")
    select_math_oper = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
    print("\nSelect a mathematical operation:")
    # друк математичної операції та її результату в залежності від вибору
    if select_math_oper == 1:
        print("Addition")
        addition = number1 + number2
        print("Result:", addition)
    elif select_math_oper == 2:
        print("Subtraction")
        subtraction = number1 - number2
        print("Result:", subtraction)
    elif select_math_oper == 3:
        print("Multiplication")
        multiplication = number1 * number2
        print("Result:", multiplication)
    elif select_math_oper == 4:
        # перевірка другого операнду - на 0 ділити не можна
        if number2 != 0:
            print("Division")
            division = number1 / number2
            print("Result:", division)
        else:
            print("You can't divide by 0")
    else:
        print("Invalid input")

        user_answer = str(input("Enter 'y' for continue:")).strip().lower()
        if user_answer != "y":
            print("Thank you for using the calculator")
            break



# ДЗ 5.3 Створити hashtag.
# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
# Декілька правил:
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

# Внесення рядка для перетворення у hashtag
input_string = input("Enter string for hashtag: ")

#перевіряємо на наявність знаків пунктуації та пробілів та видалити їх, створюємо новий рядок
# та перенаправляємо туди символи строки без пунктуації та пробілів
cleaned_string = ""
for char in input_string:
    if char not in string.punctuation and not char.isspace():
        cleaned_string += char
#print(cleaned_string)
# перевести перші літери слів у великі : спочатку кожне слово рядку перетворює на слово
# з великої букви, потім розбиваємо рядок на список слів
input_string = cleaned_string.title().split()

# обєднуємо  список слів в один рядок без роздільників і додаємо # в начало
hashtag = "".join(input_string)
hashtag = "#" + hashtag
# обмежуємо рядок 140 символами
if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)




