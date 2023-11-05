from tkinter import *


def button_clicked():
    prompt = input.get()
    mylabel.config(text=prompt)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)
# Label
mylabel = Label(text="Pornfidelity", font=("Ariel", 15))
mylabel["text"] = "Brazzers"
mylabel.config(text="Namaste")
# mylabel.pack()
# mylabel.place(x=0,y=0)
mylabel.grid(column=0, row=0)
# Buttons
button = Button(text="I am a button.", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="Variant", command=button_clicked, font=('Ariel', 15))
button1.grid(column=2,row=0)
# Entry
input = Entry(width=15)
input.grid(column=3,row=3)

window.mainloop()
