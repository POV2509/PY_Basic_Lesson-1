#ДЗ 11.1. Генератор простих чисел
# Функція-генератор prime_generator, яка повертатиме прості числа.
# Верхня межа цього діапазону визначається параметром цієї функції.

def prime_generator(n):
    """
    Generator of prime numbers.
    :param n: the upper limit of the range
    :return: prime numbers
    """
# створюємо генератор , який проходить по елементам n разів та перевіряє чи є
# член послідовності простим числом за допомогою функції prime_number: перевіряє  чи кожен
# член послідовності (починаючі з 2) не ділиться без залишку на всі члени послідовності
#v1
    #def prime_number(n):
        # if n <= 1:
        #       return False:
        # for x in range(2, n-1):
        #     if n % x == 0:
        #         return False
        # return True
#v2 замінюємо функцію prime_number, використовуємо lambda
    prime_number = lambda n: n >= 1 and all(n % x != 0 for x in range(2, n))

    for number in range(2, n+1):
        if prime_number(number):
            yield number


# друкуємо прості числа
print(list(prime_generator(20)))


# ДЗ 11.2. Заповнення списку кубами чисел
# Реалізувати функцію-генератор generate_cube_numbers, яка формує набір кубів чисел,
# починаючи з числа 2 до вказаної  величини. Тобто. генератор повинен працювати доти,
# поки генерується значення менше зазначеної величини.

def generate_cube_numbers(n):
    """
    A generator function that forms a set of cubes of numbers
    :return: list of cubes of numbers
    """
    # створюємо генератор , який проходить по елементам та обчислює
    # член послідовності -  генерує куби чисел ,  поки отриманий куб
    # числа меньше ніж вказане число.

    curent_number = 2
    while curent_number ** 3 <= n:
        cube = curent_number ** 3
        yield cube
        curent_number += 1

# створюємо генератор та друкуємо членів послідовності
list_cubes = list(generate_cube_numbers(200))
print(list_cubes)

# ДЗ 11.3. Перевірка на парність.
# Ваша функція is_even, як і раніше, повинна повертати True якщо число парне, або False
# якщо число непарне, але при цьому НЕ МОЖНА використовувати ділення у функції, та дії пов'язані
# з ним. Тобто. заборонено використовувати /, //, % та divmod
# Складність ще полягає і в тому, щоб знайти рішення, яке не залежало б від розміру числа.
# Вхідні дані: Ціле число.
# Вихідні дані: True або False

def is_even(number):
    """
    Check whether a number is even or not (without /, //, % , divmod).
    :param numeric: integer
    :return: logical type
    """
    # перевірка на парність шляхом перетворення числа на рядок, берем останню цифру та
    # перевіряєм чи є цифра у рядку "02468", якщо є
    # то число парне і функція повертає True, інакше False.
    return str(number)[-1] in "02468"

#Використання
print(is_even(20001723885652436769))
print(is_even(654423243142678))
print(is_even(9575343132433766))