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