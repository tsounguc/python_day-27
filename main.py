# import tkinter
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()
my_label.grid(row=0, column=0,)
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)


# Button
def button_clicked():
    my_label.config(text= input.get())


button = Button(text="Button", command=button_clicked)
# button.pack()
button.grid(row=1, column=1)

button = Button(text="New Button")
# button.pack()
button.grid(row=0, column=2)

# Entry

input = Entry(width=10)
input.grid(row= 2, column=3 )
# input.pack()
print(input.get())

window.mainloop()
