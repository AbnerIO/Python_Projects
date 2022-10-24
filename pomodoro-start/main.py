import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text = "Timer")
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
    countdown(work_sec)
    if reps % 8 == 0:
        timer_label.config(text="Break", bg=YELLOW, font=("Times New Roman", 24), fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", bg=YELLOW, font=("Times New Roman", 24), fg=PINK)
        countdown(short_break_sec)
    else:
        timer_label.config(text="Work", bg=YELLOW, font=("Times New Roman", 24), fg=GREEN)
        countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{str(count_sec)}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        checkmark.config(text=mark)
# ---------------------------- UI SETUP -------------------------------


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# GUI Parts
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_label = Label(text="Timer", bg=YELLOW, font=("Times New Roman", 24), fg=GREEN)
checkmark = Label(text="", bg=YELLOW, font=("Times New Roman", 24), fg=GREEN)
start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)


# Grid display
checkmark.grid(column=1, row=3)
timer_label.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

canvas.grid(column=1, row=1)




window.mainloop()
