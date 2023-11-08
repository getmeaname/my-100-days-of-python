from tkinter import *
from tkinter import messagebox
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
clock = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():
    window.after_cancel(clock)
    canvas.itemconfig(timer_txt, text="00 : 00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", font=(FONT_NAME, 24, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", font=(FONT_NAME, 24, "bold"), fg=PINK, bg=YELLOW)
        messagebox.showinfo("Break time", "Time to take a break")
    else:
        count_down(work_sec)
        timer.config(text="Work", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_txt, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        record_session = math.floor(reps / 2)
        for _ in range(record_session):
            marks += "✔"
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=canvas_img)
timer_txt = canvas.create_text(100, 130, text="00 : 00", fill="white", font=(FONT_NAME, 16, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_clock)
reset_button.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
