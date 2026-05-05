from tkinter import *
import math




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

def rest_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME, 50, "bold"))
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def star_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break!", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work!", fg=YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = "0" + str(count_sec)  #or count_sec = f"0{count_sec}

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        star_timer()
        marks = ""
        work_session = math.floor(reps / 2)

        for _ in range(work_session):
            marks += "   ✔️"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

title_label = Label(text="Timer", fg=YELLOW, bg=GREEN, font=(FONT_NAME,50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=star_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=rest_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=YELLOW, bg=GREEN, font=(FONT_NAME,30))
check_marks.grid(row=3, column=1)






window.mainloop()