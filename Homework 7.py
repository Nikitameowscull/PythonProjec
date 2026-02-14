from datetime import datetime
now = datetime.now()
print(f"Зараз: {now.strftime('%d.%m.%Y %H:%M:%S')}")

#Task 2
date_input = input("Введіть дату (дд.мм.рррр): ")
try:
    valid_date = datetime.strptime(date_input, "%d.%m.%Y")
    print("Дата коректна!")
except ValueError:
    print("Такої дати не існує або формат невірний.")

#Task 3
def calculate_age(birth_date_str):
    birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y").date()
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

b_day = input("Введіть вашу дату народження (дд.мм.рррр): ")
print(f"Ваш вік: {calculate_age(b_day)} років")

#Task 4
d1 = input("Введіть першу дату (дд.мм.рррр): ")
d2 = input("Введіть другу дату (дд.мм.рррр): ")

date1 = datetime.strptime(d1, "%d.%m.%Y")
date2 = datetime.strptime(d2, "%d.%m.%Y")

delta = abs(date2 - date1)
print(f"Різниця становить: {delta.days} днів")

#Task 5
def get_greeting():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Доброго ранку!"
    elif 12 <= current_hour < 18:
        return "Доброго дня!"
    elif 18 <= current_hour < 23:
        return "Доброго вечора!"
    else:
        return "Доброї ночі!"


print(get_greeting())

#Task 6
def str_to_datetime(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y")

user_input = input("Введіть дату для конвертації (дд.мм.рррр): ")
dt_obj = str_to_datetime(user_input)
print(f"Об'єкт створено: {type(dt_obj)} -> {dt_obj}")

#Task 7
target_input = input("Введіть майбутню дату (дд.мм.рррр): ")
target_date = datetime.strptime(target_input, "%d.%m.%Y")
today = datetime.now()

if target_date > today:
    remaining = target_date - today
    print(f"Залишилося: {remaining.days} повних днів")
else:
    print("Ця дата вже минула!")