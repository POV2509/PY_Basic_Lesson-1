# Клас Group - множина, перелік студентів, має атрибут (змінну) - номер групи.

from group_limit_reached_exception import GroupLimitReachedException
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

# Для додавання використовується метод add_student
# додано перевірку щодо досягнення максимальної кількості студентів у групі та
# використання класу GroupLimitReachedException
    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitReachedException(f"There can be no more than 10 students in a group {self.number}!")
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
