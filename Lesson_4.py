# ДЗ  4.1  Програма, яка переміщує всі нулі до кінця списку.
#          Порядок ненульових чисел має зберігатись.

# Список
#digits = [4, 13, 0, 5, 0, 99]
#digits = [0]
digits = [89, 5, 0, 0, 45, 12, 0, 1, 0, 87, 32]
print(digits)
# Створюємо пустий список, у який буде заноситись результуюча послідовність чисел.
digits_new = []
# Створюємо цикл переносу не нульових чисел у пустий список
# якщо цифра не нуль , то додаємо її у новий список
for d in digits:
    if d !=0:
        digits_new.append(d)
#проміжний перегляд списку без нулів (якщо не користуватись Debug режимом)
#print(digits_new)
# підрахунок 0 у списку
zero_count = digits.count(0)
# перегляд підрахунку кількості 0 (якщо не користуватись Debug режимом)
#print(zero_count)
# заносимо 0 у кінець нового списку (відповідно до підрахунку)
while zero_count != 0:
    zero_count -= 1
    digits_new.append(0)
print(digits_new)


# ДЗ 4.2  Знайти суму елементів із парними індексами, потім цю суму
# помножити на останній елемент списку.
# Для порожнього списку результат завжди 0.

#digits_new = []
#digits_new = [1, 0, 5, 9, 6, 2]
digits_new = [11, 5, 75, 90, 1, 1]
result_sum = 0
# визначаємо чи пустий список, шоб надрукувати результат 0, т.я. при виконанні операцій
# з індексами неіснуючих елементів - помилки
if digits_new != []:
# визначаємо парні індекси елементів списку за допомогою функції range
       for d in range(0,len(digits_new),2):
# отримаємо суму елементів списку  з парними індексами
              result_sum += digits_new[d]
# отриману суму множимо на останній елемент списку
       result = result_sum * digits_new[-1]
# друкуємо результат
       print(result)
# друк результату, якщо список пустий
else:
      print("0")



# ДЗ 4.3. Список із 3 елементів.
# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
# Cтворити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

# завантажуємо бібліотеку random для генерування випадкових чисел
import random
# створюємо список з випадковою кількістю елементів від 3 до 10
digits_random = [random.randint(3,10) for i in range(random.randint(3,10))]
# друкуємо  список
print(digits_random)
# створюємо список індексів елементів , які потрібно перенести у новий список -
# перший, третій та другий з кінця списку digit_random
indexes = [0, 2, -2]
# створюємо новий список, який складається з 3-х елементів,які зчитуємо з списку
# digit_random, а саме елементи з індексами 0,2,-2
new_digits = [digits_random[i] for i in indexes]
# друкуємо новий список
print(new_digits)

#v2
# або створення нового списку без створення списку індексів та циклу
#new_digits = [digits_random[0], digits_random[2], digits_random[-2]]