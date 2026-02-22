import tkinter as tk
import random
from tkinter import messagebox

def move_target():
    if time_left > 0:
        new_x = random.randint(0, 340)
        new_y = random.randint(0, 340)
        target.place(x=new_x, y=new_y)

def on_click():
    global score
    if time_left > 0:
        score += 1
        label_score.config(text=f"Рахунок: {score}")
        move_target()

def update_timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        label_timer.config(text=f"Час: {time_left}")
        root.after(1000, update_timer)
    else:
        target.config(state="disabled")
        messagebox.showinfo("Час вийшов!", f"Ваш результат: {score} очок")

root = tk.Tk()
root.title("Спідран Клікер")
root.geometry("400x500")

score = 0
time_left = 30

label_score = tk.Label(root, text=f"Рахунок: {score}", font=("Arial", 14))
label_score.pack(pady=5)

label_timer = tk.Label(root, text=f"Час: {time_left}", font=("Arial", 14), fg="red")
label_timer.pack(pady=5)

game_canvas = tk.Frame(root, width=400, height=400, bg="#f0f0f0", relief="ridge", bd=3)
game_canvas.pack()
target = tk.Button(game_canvas, text="НАТИСНИ МЕНЕ!!", bg="red", fg="white",
                   font=("Arial", 12, "bold"), command=on_click, width=4, height=2)
target.place(x=175, y=175)
update_timer()

root.mainloop()
