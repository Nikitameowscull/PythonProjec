#Task 1
def calculate_sum(*args):
    return sum(args)

numbers = map(float, input("Введіть числа через пробіл для суми: ").split())
print(f"Сума: {calculate_sum(*numbers)}")

#Task 2

def find_max(*args):
    return max(args) if args else "Список порожній"

numbers = map(float, input("Введіть числа через пробіл для пошуку максимуму: ").split())
print(f"Максимум: {find_max(*numbers)}")

#Task 3

def student_average(name, *grades):
    if not grades:
        return f"У студента {name} немає оцінок."
    average = sum(grades) / len(grades)
    return f"Середній бал студента {name}: {average:.2f}"

s_name = input("Введіть ім'я студента: ")
s_grades = map(int, input("Введіть оцінки через пробіл: ").split())
print(student_average(s_name, *s_grades))

#Task 4

def join_strings(*args):
    return " ".join(args)
words = input("Введіть кілька слів через пробіл: ").split()
print(f"Результат: {join_strings(*words)}")

#Task 5

def count_vowels(*args):
    vowels = "aeiouyаеєиіїоуюяAEIOUYАЕЄИІЇОУЮЯ"
    count = 0
    for string in args:
        for char in string:
            if char in vowels:
                count += 1
    return count
strings = input("Введіть рядки для підрахунку голосних: ").split()
print(f"Кількість голосних: {count_vowels(*strings)}")

#Task 6

def get_squares(*args):
    return [x**2 for x in args]

numbers = map(float, input("Введіть числа для піднесення до квадрату: ").split())
print(f"Квадрати: {get_squares(*numbers)}")

#Task 7

def merge_lists(*args):
    result = []
    for lst in args:
        result.extend(lst)
    return result
list1 = input("Введіть елементи першого списку: ").split()
list2 = input("Введіть елементи другого списку: ").split()
print(f"Об'єднаний список: {merge_lists(list1, list2)}")

#Task 8

def calculate_product(*args):
    if not args:
        return 0
    res = 1
    for n in args:
        res *= n
    return res

numbers = map(float, input("Введіть числа для обчислення добутку: ").split())
print(f"Добуток: {calculate_product(*numbers)}")