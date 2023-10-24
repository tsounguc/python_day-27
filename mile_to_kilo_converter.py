from tkinter import *


def calculate_km():
    miles_value = float(miles_input.get())
    km_value = round(miles_value * 1.609, 2)
    km_result_label.config(text=f"{km_value}")


window = Tk()

window.title("Mile to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=75)

miles_input = Entry(width=12)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("Arial", 14, "bold"))
miles_label.grid(row=0, column=2)
miles_label.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_to.grid(row=1, column=0)
is_equal_to.config(padx=10, pady=10)

km_result_label = Label(text="0", font=("Arial", 14, "bold"))
km_result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("Arial", 14, "bold"))
km_label.grid(row=1, column=2)

button = Button(text="Calculate", command=calculate_km)
button.grid(row=2, column=1)

window.mainloop()
