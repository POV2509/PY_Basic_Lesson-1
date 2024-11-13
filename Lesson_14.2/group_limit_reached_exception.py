# Клас GroupLimitReachedException - для опису винятку щодо досягнення ліміту кількості студентів
# з наслідуванням стандартного класу винятків Exception шоб створити спеціалізований виняток (ліміт кількості студентів)

class GroupLimitReachedException (Exception):
    def __init__(self, message):
       #self.message = message
       super().__init__(message)


