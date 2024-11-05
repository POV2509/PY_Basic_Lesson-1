#ДЗ 10.1. Генераторна функція
#Реалізувати генераторну функцію (з використанням оператора yield), яка повертатиме
# по одному члену числової послідовності, закон якої задається за допомогою функції
# користувача. Крім цього параметром генераторної функції повинні бути значення
# першого члена прогресії та кількість членів, що видаються послідовності (n).
# Генератор повинен зупинити свою роботу з досягнення n-го члена.

#
def my_generator(first_number, n, geometric_progression):
    """
    generator function
    :return: numbers geometric progression
    """
    # створюємо генератор , який проходить по елементам n разів та обчислює кожен раз
    # член послідовності за допомогою функції geometric progression: кожен наступний член
    # є квадратом попереднього
    curent_number = first_number
    for i in range(n):
        yield curent_number
        curent_number = geometric_progression(curent_number)

# функція геометрична прогресія за допомогою lambda (обчислення члена послідовності)
geometric_progression = lambda y : y ** 2

# створюємо генератор та друкуємо членів послідовності
for number in my_generator(2, 5, geometric_progression):
    print(number)


#ДЗ 10.2. Знайти перше слово
#Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
#У рядку можуть зустрічаються крапки та/або коми
#Рядок може починатися з літери або, наприклад, з пробілу або точки
#У слові може бути апостроф і він є частиною слова
#Весь текст може бути представлений лише одним словом та все
#Вхідні параметри: Рядок.Вихідні параметри: Рядок.

def first_world(line):
    """
    Find the first word.
    :param: string
    :return: string
    """
    # видалимо зліва (на початку рядку ) пробіли, точки та коми
    line = line.lstrip("., ")
    # поділимо рядок на слова за пробілами
    words = line.split()

    # видаляємо розділові знаки з початку та кінця кожного слова за допомогою функції map
    cleaned_words = list(map(lambda word: word.strip("., "), words))
    # повертаємо перше слово (з нульовим індексом) якщо воно є або повідомлення, якщо нема
    return cleaned_words[0] if cleaned_words else "The world is absent!"


print(first_world("  .Hel`lo, all!"))
print(first_world(",."))
print(first_world("  ..,,ho, ,ho, ,ho"))



# ДЗ 10.3. Перевірити чи є парним чи ні
# Функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.

def is_even(number):
    """
    Check whether a number is even or not.
    :param numeric: integer
    :return: logical type
    """
    # перевірка на парність шляхом поділу на 2 (оператор %) та визначення залишку , якщо
    # залишок 0 то функція повертає True, інакше False.
    return number % 2 == 0

#Використання
print(is_even(20001))
print(is_even(60))
print(is_even(99))

