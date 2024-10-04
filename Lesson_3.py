# ДЗ 3.1 Найпростіший калькулятор.
# Виконання 4-х математичних дій (+,-,*,/) з двома операндами.
# + виконати перевірку другого операнда - при діленні не повинен бути 0

## Варіант1 - з використанням оператора elif

# введення чисел - визначення зміних (перший та другий операнд)
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
# введення переліку математичних операцій
print("\nCalculator")
select_math_oper = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
print("\nSelect a mathematical operation:")
#друк математичної операції та її результату в залежності від вибору
if select_math_oper == 1:
    print("Addition")
    addition = number1 + number2
    print("Result:",addition)
elif select_math_oper == 2:
    print("Subtraction")
    subtraction = number1 - number2
    print("Result:",subtraction)
elif select_math_oper == 3:
    print("Multiplication")
    multiplication = number1 * number2
    print("Result:",multiplication)
elif select_math_oper == 4:
#перевірка другого операнду - на 0 ділити не можна
    if number2 != 0:
        print("Division")
        division = number1 / number2
        print("Result:", division)
    else:
        print("You can't divide by 0")
else:
    print("Invalid input")


## Варіант2 з використанням конструкції match

# введення чисел - визначення зміних (перший та другий операнд)
number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
# введення переліку математичних операцій
print("\nCalculator")
select_math_oper = int(input("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
print("\nSelect a mathematical operation:")
#друк математичної операції та її результату в залежності від вибору
match select_math_oper:
    case 1:
        print("Addition")
        addition = number1 + number2
        print("Result:",addition)
    case 2:
        print("Subtraction")
        subtraction = number1 - number2
        print("Result:",subtraction)
    case 3:
        print("Multiplication")
        multiplication = number1 * number2
        print("Result:",multiplication)
    case 4:
#перевірка другого операнду - на 0 ділити не можна
        if number2 != 0:
            print("Division")
            division = number1 / number2
            print("Result:", division)
        else:
            print("You can't divide by 0")
    case _:
        print("Invalid input")


# ДЗ 3.2 Перемістити останній елемент у списку на початок.

print("Lists :")
digits = [10, 20, 30, 40, 50]
#digits = [10]
#digits = []  # при нульовому списку - помилка у 82 рядку - index out of range
print(digits)
# вставлено за допомогою функції insert останній елемент [-1] списку  у список по індексу 0
digits.insert(0,digits[-1])
# видалено останній елемент списку за допомогою функції pop()
digits.pop()
# друк результуючого списку
print(digits)



# ДЗ 3.3  Розділити один список на два списки та помістити їх у новий список.
# Якщо в початковому списку непарна кількість елементів, то в першому списку має бути більше елементів.
# Якщо у списку немає елементів, то має бути створений список із двома порожніми списками.


print("Lists :")
#digits = [10, 20, 30, 40, 50, 60]
digits = [10, 20, 30, 40, 50]
#digits = [10]
#digits = []
print(digits)
# перевіряємо кількість елементів у списку : парне чи непарне
if len(digits) % 2 == 0:
# парна кількість елементів
# розраховуємо індекс останнього елементу першого списку шляхом поділу кількості елементів списку (фун-я len) націло на 2
    first_list = digits[:len(digits) // 2]
#розраховуємо індекс першого елементу другого списку шляхом поділу кількості елементів списку (фун-я len) націло на 2
    second_list = digits[len(digits) // 2:]
# формуємо список з двох списків
    shared = [first_list, second_list]
    print(shared)
else:
# непарна кількість елементів
# розраховуємо індекс останнього елементу першого списку шляхом поділу кількості елементів списку (фун-я len) націло на 2
    first_list = digits[:len(digits) // 2+1]
#розраховуємо індекс першого елементу другого списку шляхом поділу кількості елементів списку (фун-я len) націло на 2
    second_list = digits[len(digits) // 2+1:]
# формуємо список з двох списків
    shared = [first_list, second_list]
    print(shared)
