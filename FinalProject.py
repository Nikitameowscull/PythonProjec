import tkinter as tk
from tkinter import messagebox

data = {
    "Monza": {
        "Ferrari 296 GT3": "Tyres: 26.5 PSI | Wing: 2 | BB: 54%",
        "Porsche 911 GT3 R": "Tyres: 26.8 PSI | Wing: 1 | BB: 52%",
        "Lamborghini Huracan": "Tyres: 26.7 PSI | Wing: 3 | BB: 55%"
    },
    "Spa-Francorchamps": {
        "Ferrari 296 GT3": "Tyres: 26.9 PSI | Wing: 6 | BB: 56%",
        "Porsche 911 GT3 R": "Tyres: 27.0 PSI | Wing: 5 | BB: 53%",
        "Lamborghini Huracan": "Tyres: 26.8 PSI | Wing: 7 | BB: 57%"
    },
    "Zolder": {
        "Ferrari 296 GT3": "Tyres: 26.7 PSI | Wing: 9 | BB: 53%",
        "Porsche 911 GT3 R": "Tyres: 26.6 PSI | Wing: 10 | BB: 51%"
    }
}


def update_cars(event):
    if not track_list.curselection():
        return

    selected_track = track_list.get(track_list.curselection())
    car_list.delete(0, tk.END)

    for car in data[selected_track].keys():
        car_list.insert(tk.END, car)


def show_setup():
    if not track_list.curselection() or not car_list.curselection():
        messagebox.showwarning("Увага", "Спочатку обери ТРАСУ, а потім АВТОМОБІЛЬ!")
        return

    track = track_list.get(track_list.curselection())
    car = car_list.get(car_list.curselection())
    setup = data[track][car]
    messagebox.showinfo(f"{car} @ {track}", setup)


root = tk.Tk()
root.title("ACC Master Setup")
root.geometry("600x500")
root.configure(bg="#0a0a0b")

main_frame = tk.Frame(root, bg="#0a0a0b")
main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

left_frame = tk.Frame(main_frame, bg="#0a0a0b")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

tk.Label(left_frame, text="1. ОБЕРИ ТРАСУ", font=("Arial", 11, "bold"), fg="#ff1e00", bg="#0a0a0b").pack()
track_list = tk.Listbox(left_frame, font=("Arial", 11), bg="#161618", fg="white",
                        selectbackground="#ff1e00", borderwidth=0, highlightthickness=1)
for t in data.keys():
    track_list.insert(tk.END, t)
track_list.pack(fill=tk.BOTH, expand=True, pady=10)
track_list.bind("<<ListboxSelect>>", update_cars)

right_frame = tk.Frame(main_frame, bg="#0a0a0b")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

tk.Label(right_frame, text="2. ОБЕРИ АВТОМОБІЛЬ", font=("Arial", 11, "bold"), fg="#ff1e00", bg="#0a0a0b").pack()
car_list = tk.Listbox(right_frame, font=("Arial", 11), bg="#161618", fg="white",
                      selectbackground="#ff1e00", borderwidth=0, highlightthickness=1)
car_list.pack(fill=tk.BOTH, expand=True, pady=10)

btn = tk.Button(root, text="ПОКАЗАТИ НАЛАШТУВАННЯ", command=show_setup,
                font=("Arial", 11, "bold"), bg="#ff1e00", fg="white",
                activebackground="#cc1800", relief="flat", pady=15, cursor="hand2")
btn.pack(side=tk.BOTTOM, fill=tk.X, padx=30, pady=20)

root.mainloop()