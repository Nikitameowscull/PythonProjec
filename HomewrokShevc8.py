#task 1
import tkinter as tk

WIN_TITLE = "Програма Виходу"
BTN_TEXT = "Вихід"
WIN_SIZE = "300x200"
root = tk.Tk()
root.title(WIN_TITLE)
root.geometry(WIN_SIZE)
exit_button = tk.Button(root, text=BTN_TEXT, command=root.destroy)
exit_button.pack(expand=True)

root.mainloop()

#task 2
def update_label():
    text_from_entry = entry.get()
    label.config(text=f"Ви написали: {text_from_entry}")
BTN_CONFIRM = "Підтвердити"
START_TEXT = "Тут з'явиться ваш текст"

root = tk.Tk()
root.title("Ввід тексту")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

btn = tk.Button(root, text=BTN_CONFIRM, command=update_label)
btn.pack(pady=5)

label = tk.Label(root, text=START_TEXT)
label.pack(pady=10)

root.mainloop()

#task 3
from tkinter import messagebox

def show_choice():
    messagebox.showinfo("Вибір мови", f"Обрана мова: {lang_var.get()}")

root = tk.Tk()
root.title("Вибір мови")

lang_var = tk.StringVar(value="Українська")
languages = ["Українська", "English", "Deutsch"]

tk.Label(root, text="Оберіть мову:").pack(anchor="w", padx=10)

for lang in languages:
    tk.Radiobutton(root, text=lang, variable=lang_var, value=lang, command=show_choice).pack(anchor="w", padx=20)

root.mainloop()

#task 4


def show_date():
    messagebox.showinfo("Дата", f"Ваш вибір: {day_var.get()}, {month_var.get()}")

root = tk.Tk()
root.title("Вибір дати")

days = [str(i) for i in range(1, 32)]
months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень"]

day_var = tk.StringVar(value=days[0])
month_var = tk.StringVar(value=months[0])

tk.Label(root, text="День:").grid(row=0, column=0, padx=10, pady=10)
tk.OptionMenu(root, day_var, *days).grid(row=0, column=1)

tk.Label(root, text="Місяць:").grid(row=1, column=0, padx=10, pady=10)
tk.OptionMenu(root, month_var, *months).grid(row=1, column=1)

tk.Button(root, text="Показати дату", command=show_date).grid(row=2, columnspan=2, pady=10)

root.mainloop()

#task 5
def on_click(button_text):
    if button_text == "=":
        try:

            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Помилка")
    elif button_text == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, button_text)

root = tk.Tk()
root.title("Калькулятор")

display = tk.Entry(root, font=("Arial", 18), justify='right', bd=10)
display.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for btn_txt in buttons:
    action = lambda x=btn_txt: on_click(x)
    tk.Button(root, text=btn_txt, width=5, height=2, font=("Arial", 14), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()