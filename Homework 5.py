user_string = input("Введіть будь-який текст: ")
print(f"Результат:\n{user_string[::-1]}\n")

#Task 2

start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

for i in range(start, end + 1):
    print(f"{i}\n")

#Task 3

user_price = float(input("Введіть ціну (можна з багатьма знаками після коми): "))
print(f"Сума до сплати: {user_price:.2f} грн")

#Task 4

user_words = input("Введіть три (або більше) слова через пробіл: ").split()
print("\t".join(user_words))

#Task 5

a_val = input("Введіть значення для a: ")
b_val = input("Введіть значення для b: ")

print("Змінна a = {}, змінна b = {}".format(a_val, b_val))

#Task 6

user_text = input("Введіть текст для вирівнювання: ")
width = int(input("Введіть загальну ширину рядка (наприклад, 50): "))

print(user_text.center(width))