# Клас Student успадковує клас Human і додає новий атрібут (змінну) - залікову книжку (record_book).

from human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

# метод (функція) __str__ перевизначається, т.я. потрібно надрукувати всю інформацію про студента, включаючи
# номер залікової книжки (у текстовому форматі).
    def __str__(self):
        return f" {super().__str__()}, Record_book: {self.record_book}"

# згідно з умовою задачі необхідно додати метод(функцію) порівняння студентів та метод _hash_.
# Метод _eq_ перевіряє, чи є об’єкт other екземпляром класу Student за допомогою
# функції isinstance()) .

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str (other)
        return False

    def __hash__(self):
        return hash(str(self))

