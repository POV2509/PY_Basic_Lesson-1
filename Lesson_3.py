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
