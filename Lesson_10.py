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


