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

#ДЗ 7.3. Пошук підрядка
# Функція second_index приймає як параметри 2 рядки. Необхідно знайти індекс
# другого входження шуканого рядка у рядку для пошуку.
# Input: Два рядки (String). Output: Int or None

def second_index (line: str, subline:str) -> int:
# шукаємо індекс першого входження за допомогою метода find
    find_first = line.find(subline)
# якщо першого входження нема, то None
    if find_first == -1:
        return None
# шукаємо індекс другого входження, з позиції після першого входження
    find_second = line.find(subline, find_first + len(subline))
# якщо другого входження нема, то None
    if find_second != -1:
        return find_second
    else: None

# Застосовуєм
print(second_index("hohoho","ho"))
print(second_index("Hello all","ll"))
print(second_index("Hello hello","lo"))


#ДЗ 7.4. Пошук спільних елементів
#Функція common_elements, яка згенерує два списки елементів з генераторного виразу (range)
# для 100 елементів,за наступними правилом: один список з числами кратними 3,
#інший з кратними числами 5.
#За допомогою множин створіть набір з числами, які є в обох множинах (перетин).
#Функція повинна повернути цю множину як результат своєї роботи.

def common_elements() -> set:
# Генеруємо множину чисел, кратних 3 з рандомного списку з 100 елементів
    multiple_of_3 = {n for n in range(100) if n % 3 == 0}
# Перегляд множини чисел, кратних 3 (для наочності)
#print(multiple_of_3)

# Генеруємо множину чисел, кратних 5 з рандомного списку з 100 елементів
    multiple_of_5 = {n for n in range(100) if n % 5 == 0}
# Перегляд множини чисел, кратних 3 (для наочності)
#print(multiple_of_5)

# Знаходимо спільні елементи двох множин за допомогою метода intersection
    common_set = multiple_of_3.intersection(multiple_of_5)

    return common_set

#Використання
print(common_elements())

