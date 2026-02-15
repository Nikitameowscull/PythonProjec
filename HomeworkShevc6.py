import os

path_to_scan = "."
files_and_dirs = os.listdir(path_to_scan)
print(f"Вміст директорії '{path_to_scan}':")
for item in files_and_dirs:
    print(f" - {item}")

#Task 2

folder_name = int(input("NewFolder"))
os.makedirs(folder_name, exist_ok=True)
print(f"Директорія '{folder_name}' готова до роботи!")

#task 3

source = "files/data.txt"
destination = "backup/data_copy.txt"
os.makedirs(os.path.dirname(destination), exist_ok=True)

shutil.copy2(source, destination)
print(f"Файл скопійовано з {source} у {destination}")

#Task 4
old_path = int(input("Old path".txt))
new_path = int(input("New data path".txt))

if os.path.exists(old_path):
    os.rename(old_path, new_path)
    print(f"Файл '{old_path}' тепер називається '{new_path}'")
else:
    print("Помилка: Файл для перейменування не знайдено.")

#Task 5

file_to_move = "important_data.txt"
target_dir = "backup/"
os.makedirs(target_dir, exist_ok=True)

shutil.move(file_to_move, os.path.join(target_dir, file_to_move))
print(f"Файл '{file_to_move}' успішно переїхав у '{target_dir}'")