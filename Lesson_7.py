#  ДЗ 7.1. Вітання
# Написати функцію say_hi, яка представить людину за переданими параметрами.
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
# Функція має повернути рядок.

# Функція має  2 аргументи: ім'я - рядок, вік - ціле число
def say_hi(name: str, age: int) -> str:
# вік повинен бути більше нуля, якщо , буде умова не буде виконана,то assert виведе текстове повідомлення (AssertionError)
    assert age > 0, "age must be an integer"
    return(f"Hi. My name is {name} and I`m {age} years old." )

# Використання
print(say_hi("Tom", 32))
print(say_hi("Jerry", 20))
#print(say_hi("Tom", 0))


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