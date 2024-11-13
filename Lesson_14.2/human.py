# Клас Humen - основний для опису людини, має конструктор , який приймає аргументи (змінні):
# стать, вік, ім`я та прізвище.
# метод (функція) __str__ друкує інформацію про людину у текстовому форматі

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender} "