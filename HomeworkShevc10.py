import re

text = "Сьогодні наше сонце світить дуже яскраво, скоро весна."
result = re.findall(r'\b[сС]\w+', text)
print(result)

#Task 2

text = "Контакти: user@example.com, info@test.org."
result1 = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print(result1)

#Task 3

text = "У мене є 2 яблука та 15 груш."
result2 = re.sub(r'\d+', 'NUMBER', text)
print(result2)

#Task 4

text = "Відвідайте http://google.com або https://python.org."
result3 = re.findall(r'https?://[\w\.-]+\.\w+', text)
print(result3)

#task 5

text = "Київ — це столиця України. Peter lives here."
result4 = re.findall(r'\b[А-ЯA-Z][а-яa-z]*', text)
print(result4)

#Task 6

text = "Код (123), версія (45), текст без дужок 78."
result5 = re.findall(r'\((\d+)\)', text)
print(result5)

#Task 7

text = "Мій номер 123-4567, а його 987-6543."
result6 = re.sub(r'\d{3}-\d{4}', 'PHONE', text)
print(result6)

