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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# GUI Parts
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
timer_label = Label(text="Timer", bg=YELLOW, font=("Times New Roman", 24), fg=GREEN)
checkmark = Label(text="✔", bg=YELLOW, font=("Times New Roman", 24), fg=GREEN)
start_button = Button(text="Start")
reset_button = Button(text="Reset")

# Grid display
checkmark.grid(column=1, row=3)
timer_label.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

canvas.grid(column=1, row=1)




window.mainloop()
