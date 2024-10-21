
# ДЗ 8.1. Додати 1 до числа
# написати функцію add_one, яка приймає список із цифр, які у свою чергу є одним числом. До нього необхідно додати 1.
# Тобто. Вам необхідно з набору цифр, що входять до списку, отримати число, скласти його з 1 і отриману суму, знову розбити на список із цифр.
# В результаті функція повертає список із цифр, що становлять значення суми.

# для формування списку будемо генерувати випадковий список чисел
# завантажуємо бібліотеку random для генерування випадкових чисел
import random
# створюємо функцію генерації списку з кількістю елементів 4 , у діапазоні від 5 до 9
def generate_digits():
   return [random.randint(5,9) for i in range(4)]
# друкуємо отриманий список
random_digits = generate_digits()
print(f"Випадковий список цифр: {random_digits}")
# створюємо функцію add_one
def add_one(random_digits):
# перетворюємо список цифр на рядок (функція map кожну цифру перетворює на рядок),
# потім на ціле число (join з`єднує рядки, int перетворює результуючий рядок на ціле число)
    number = int(''.join(map(str,random_digits)))
# додаємо 1
    number += 1
# перетворюємо число на список цифр: number у строку, кожна цифра цієї строки стає цілим числом
    return [int(digit) for digit in str(number)]

# додаємо 1 до числа, створеного рандомно з 4х цифр шляхом виклику функції add_one
result = add_one(random_digits)
# Друкуємо результат
print(f"Result: {result}")