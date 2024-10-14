# ДЗ 5.1  Ім`я змінної. Ціль - перевірка чи може довільний рядок бути іменем змінної
# Змінна не може: починатися з цифри , містити великі літери, пробіл і знаки пунктуації,
# окрім нижнього підкреслення "_", бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
# пробіл і знаки пунктуації можна взяти з string.punctuation;
# cписок зареєстрованих слів можна взяти із keyword.kwlist.

# завантажимо модуль string, буде використовуватись для перевірки на наявність пробілов
# та знаків пунктуації
import string
# завантажимо модуль keyword, буде використовуватись для перевірки на наявність зареєстрованих слів
import keyword
# створимо тестовий перелік варіантів імен змінних
variable_names_for_check = ["_", "__", "sum", "x", "get_value", "get value", "get!value", "some_super_puper_value",
                         "Get_value", "get_Value", "getValue", "3m", "m3", "assert", "assert__exception"]
#variable_names_for_check = ["some_super_puper_value"]


for name_for_check in variable_names_for_check:
# перевіряємо чи є хоч один символ у імені змінної, шоб мало сенс подальші перевірки
    if len(name_for_check) > 0 :
# перевіряємо чи є один символ "_" у імені змінної (виключення)
        if name_for_check[0] == "_" and len(name_for_check) == 1:
            print(f"Variable name '{name_for_check}' is correct!")
#перевіряємо на зареєстровані слова (keyword.kwlist)
        elif name_for_check in keyword.kwlist:
                print(f"Variable name '{name_for_check}' is in the keyword (reserved keyword)!")
        else:
# перевіряємо шоб змінна не починалась з цифри,  взагалі не містила  великих букв та пробілів
                if not name_for_check[0].isdigit() and name_for_check.islower() and not name_for_check.count(" ") != 0:
                    for s in string.punctuation.replace("_", ""):
                        if s in name_for_check:
                            print(f"Found '{s}'. Variable name '{name_for_check}' is not correct! ")
                            break
#  перевіряємо чи є підряд підкреслення:
                        elif "_" in name_for_check:
                            for i in range(len(name_for_check) - 1):
                                    if name_for_check[i] == "_" and name_for_check[i + 1] == "_":
                                        print(f"Variable name '{name_for_check}' is not correct! has several underscores in a row!")
                                    break
                        print(f"Variable name '{name_for_check}' is correct!")
                        break
                else:
                    print(f"Variable name '{name_for_check}' is not correct!")
    else:
        print(f"Variable length '{name_for_check}' is not correct!")









