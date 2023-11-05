from tkinter import *


def calc():
    prompt = to_convert.get()
    Kilometer = float(prompt) * 1.609
    round_km = round(Kilometer, 2)
    ans.config(text=round_km)


window = Tk()
window.title("miles to km Calculator")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)
# Is equal to label
is_equal = Label(text="is equal to", font=("Ariel", 12))
is_equal.grid(column=0, row=1)
# ans label
ans = Label(text="0", font=("Ariel", 12))
ans.grid(column=1, row=1)
ans.config(padx=20, pady=20)
# Miles label
miles = Label(text="Miles", font=("Ariel", 12))
miles.grid(column=2, row=0)
# miles.config(padx=20,pady=20)
# KM label
km = Label(text="Km", font=("Ariel", 12))
km.grid(column=2, row=1)
# km.config(padx=20,pady=20)
# Calc Button
button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)
# Entry button
to_convert = Entry(width=15)
to_convert.grid(column=1, row=0)

window.mainloop()
