# ДЗ 13.1. Група студентів
#Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).
#На його основі створіть клас Студент (перевизначте метод виведення інформації).
#Створіть клас Група, екземпляр якого складається з об'єктів класу Студент.
#Реалізуйте методи додавання, видалення студента та метод пошуку студента на прізвище.
#Метод пошуку студента повинен повертати саме екземпляр класу Студент, якщо студент є у групі,
# інакше - None.
#У методі видалення, використовуйте результат методу пошуку. Тобто. потрібно скомбінувати ці два методи;)
#Визначте для групи метод str() для повернення списку студентів у вигляді рядка.
# Заповнюємо надані заголовки.

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

# Клас Student успадковує клас Human і додає новий атрібут (змінну) - залікову книжку (record_book).

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    # метод (функція) __str__ перевизначається, т.я. потрібно надрукувати всю інформацію про студенат, включаючи
    # номер залікової книжки (у текстовому форматі).
    def __str__(self):
        return f" {super().__str__()}, Record_book: {self.record_book}"

# Клас Group - множина, перелік студентів, має атрибут (змінну) - номер групи.
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

# Для додавання використовується метод add_student
    def add_student(self, student):
        self.group.add(student)
# Для видалення використовується метод delete_student
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
            return True
        return False

#Для пошуку студента  за прізвищем використовується метод (функція)
# find_student. Якщо студент не знайдений - повертає None.
    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None
# Метод (функція) __str__ повертає список студентів у вигляді рядка
    def __str__(self):
        if not self.group:
            return f"У групі {self.number} студенти відсутні."
        all_students = "\n".join (str(student) for student in self.group)
        return f"Group number:{self.number}\n {all_students}"

# Використовуємо - перелік студентів
st1 = Student("Male", 18, "Tom", "Cruz", 'RB11')
st2 = Student("Female", 20, "Ann", "Smith", "RB22")
st3 = Student("Female", 21, "Bob", "White", "RB33")

group = Group("AM1")
group.add_student(st1)
group.add_student(st2)
print(group)

group.add_student(st3)
print(group)

group.delete_student("Cruz")
group.delete_student("Black")
print(group)




