#ДЗ 9.1. Визначити популярність певних слів у тексті
# на вхід функції popular_words передаються два аргументи: текст та список слів, популярність
# яких необхідно визначити.
# Слова необхідно шукати у всіх регістрах. Тобто. якщо необхідно знайти слово "one",
# значить для нього будуть підходити слова "one", "One", "oNe", "ONE" і т.д.
# Шукані слова завжди вказані в нижньому регістрі
# Якщо слово не знайдено жодного разу, його необхідно повернути у словнику зі значенням 0 (нуль)
#Вхідні параметри: Текст і масив слів, що шукаються.
#Вихідні параметри: Словник, у якому ключами є шукані слова та значеннями, скільки разів кожнє слово
# зустрічаються у орігінальному тексті.

def popular_words(text, words):
    """
    To define popularity of certain words in text.
    :param text and an array of search terms
    :return: A dictionary in which the keys are the searched words and the meanings,
    how many times each word occurs in the original text
    """

def popular_words(line_text, words):
    # Перетворюємо текст у нижній регістр
    line_text = line_text.lower()
    # перегляд для наочності
    #print(f"Перетворення у нижній регістр:  {line_text}")
    # Розбиваємо текст на слова
    word_list = line_text.split()
    # перегляд для наочності
    #print(f"Розбиваємо текст на перелік слів: {word_list}")
# v1
    # Функція для підрахунку входжень слова
    #def count_word(word):
    #    return (word, word_list.count(word))
    # Використовуємо функцію map для підрахунку входжень кожного слова, потім використовуємо
    # функцію list для перетворення об'єкту map у список
    #result = list(map(count_word, words))
# v2 зберемо все в кучку
    result = list(map(lambda word: (word, word_list.count(word)), words))
    return result

# Приклад використання
text = "One Two Three one tWo thRee oNe TWO tHrEE"
print(text)
words = ["one", "two", "three"]
print(words)
print(f"Рopularity of words in the text: {popular_words(text, words)}")


# ДЗ 9.2. Різниця між числами
# Є набір чисел (float або int).Потрібно знайти різницю між найбільшим і найменшим
# елементом. Функція difference має вміти працювати з невизначеною кількістю
# аргументів. Якщо аргументів немає, то функція повертає 0 (нуль).
# Для округлення використовуйте функцію round(x, 2).
# Вх. Дані: Змінна кількість аргументів як числа (int, float).
# Вих. Дані: Різниця між максимумом і мінімумом як число (int, float).

def difference(*args):
    """
    The difference between the numbers.
    :param args:A variable number of arguments as numbers (int, float).
    :return:Difference between maximum and minimum as number (int, float).
    """
    # перевіряємо чи є аргументи, якщо нема=> 0
    if not args:
        return print("Number of arguments: 0")
    # визначаємо максимальне та мінімальне число
    max_args = max(args)
    min_args = min(args)
    # знаходимо різницю між max та min та округлюємо результат до 2 знаків після запятой
    return round(max_args - min_args, 2)

print(f"Difference between max and min: {difference(1, 3, 11, 10.111, 99)}")
print(f"Difference between max and min: {difference(1, 3, 11, 101.111, 99)}")
print(f"Difference between max and min: {difference ()}")
print(f"Difference between max and min: {difference(1.99999, 3, 11, 10.111, 99)}")
