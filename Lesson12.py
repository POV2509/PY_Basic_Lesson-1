# ДЗ 12.1. Очистити текст від html-тегів
#Написати функцію, яка прочитає заданий файл, очистить текст від html-тегів і запише цей текст в інший файл.
#html-тег завжди починається з "<" і закінчується на ">" ,потрібно видалити ці символи та все, що між ними.
#Функція отримує на вхід два параметри – ім'я файлу, який потрібно очистити, та ім'я файлу, куди потрібно
# записати очищений текст. Ім'я файлу, куди потрібно писати, можна задати за замовчуванням.
#Приклади файлів у вкладенні – файл який потрібно очистити (draft.html) та приклад файлу,
# який може вийти на виході з очищеним текстом (cleaned.txt). Файл draft.html необхідно скачати і
# покласти поряд з файлом, де буде вирішення цієї задачі.

# для використання регулярних виразів завантажуємо бібліотеку re
import re

def cleaner_htmlteg(input, output):
    """
    Clean the text from html tags.
    input : input_file , name output_file
    output : output_file without tegs
    """
    # читаємо файл draft.html
    with open(input, "r") as file:
        text = file.read()
    # по суті, нам потрібно вивести зміст, що розміщено у тегах => шукаємо зміст, який розміщено
    # між символами > та </ за допомогою регулярного виразу
    template = r">(.*)</"
    #для пошуку використовуємо функцію findall, яка знаходить та повертає усі збіги з шаблоном
    matches = re.findall(template, text)
    # знайдене співпадіння необхідно записати у файл та розділити по рядкам (\n )
    with open(output, "w") as file:
        for match in matches:
            text = file.write(match + "\n")
# Використовуємо
cleaner_htmlteg("draft.html", "cleaned_file.txt")

#ДЗ 12.2. Корзина для покупок
# Створіть клас для опису товару. Як поля товару можете використовувати значення ціни, опис, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
# Створіть клас "Покупець". Як поля можна використовувати прізвище, ім'я, по батькові, мобільний телефон і т.д.
# Створіть клас "Замовлення". Замовлення може містити кілька товарів, причому кількість кожного з товарів
# може бути різною. Замовлення має бути "підв'язане" до користувача, який його здійснив. Реалізуйте метод
# обчислення сумарної вартості замовлення. Визначте метод str() для коректного виведення інформації про
# це замовлення.

# Створюємо клас для опису товара з атрибутами: назва, ціна, опис, розмір
class Product:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    # використовуємо метод str шоб отримати рядок та вивести його
    def __str__(self):
        return f"{self.name}, price: {self.price} $"

# Створюємо клас покупця з атрибутами ім`я, прізвище, номер телефону
class Buyer:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    # використовуємо метод str шоб отримати рядок та вивести його
    def __str__(self):
        return f"{self.name.title()} {self.surname.title()}"

# Створюємо клас замовлення
class Order:

    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    # створюємо функцію додавання товару (у словник products): товар, кількість у шт.
    def add_item(self, item, cnt):
        self.products[item] = cnt
    # строкове представлення замовлення
    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products += f"\n{product.name}: {count} pcs."
        return f"\nOrder\nBuyer: {self.user}\nProducts:{all_products}"

    # функція підрахунку товарів
    def get_total(self):
        all_sum = 0
        for product, count in self.products.items():
            all_sum += (product.price * count)
        return f"Total:{all_sum} $"

# визначаємо атрибути для екземпляру замовлення : товари та покупець
pear = Product("pear", 1, "green", "big")
print(pear)
avocado = Product("avocado", 2, "red", "middle")
print(avocado)
buyer = Buyer("Taras", "Melnik", "0123456789")
print(buyer)
# формуємо замовлення
cart = Order(buyer)
cart.add_item(pear, 10)
cart.add_item(avocado, 2)
print(cart)
print(cart.get_total())

