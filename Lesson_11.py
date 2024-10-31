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
