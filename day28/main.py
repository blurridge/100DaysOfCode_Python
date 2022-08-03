# Main

from tkinter import *
import math

RED = "#FF1E00"
GREEN = "#59CE8F"
BG_COLOR = "#E8F9FD"
TEXT_COLOR = "#000000"
FONT_NAME = "Helvetica"
WORK_TIME = 25
SHORT_BREAK = 5
LONG_BREAK = 20
MAX_REPS = 7
reps = 0
curr_progress = ""
timer = NONE

# TIMER

def start_timer():
    global reps
    reps+=1
    if reps > MAX_REPS:
        count_down(LONG_BREAK * 60)
        timer_label.config(text="Long Break", fg=GREEN)
    elif reps % 2 == 1:
        count_down(WORK_TIME * 60)
        timer_label.config(text="Work", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK * 60)
        timer_label.config(text="Short Break", fg=GREEN)

# RESET

def reset_app():
    global curr_progress, timer, reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=TEXT_COLOR)
    canvas.itemconfig(timer_clock, text="00:00")
    reps = 0
    timer = NONE
    curr_progress = ""
    progress_text.config(text=curr_progress)

# COUNTDOWN

def count_down(count):
    global timer
    hour = math.floor(count/60) if math.floor(count/60) >= 10 else f"0{math.floor(count/60)}"
    minute = count % 60 if count % 60 != 0 and count % 60 >= 10 else f"0{count%60}"
    canvas.itemconfig(timer_clock, text=f"{hour}:{minute}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif reps <= MAX_REPS:
        add_progress()
        start_timer()
    else:
        add_progress()

# PROGRESS

def add_progress():
    global curr_progress
    symbols = ["✔", "⏰", "⭕"]
    if reps > MAX_REPS:
        curr_progress+=symbols[2]
    elif reps%2 == 1:
        curr_progress+=symbols[0]
    elif reps%2 == 0 and reps != 0:
        curr_progress+=symbols[1]
    progress_text.config(text=curr_progress)

# UI

window = Tk()
window.title("Pomodoro App by blurridge")
window.config(padx=50, pady=25, bg=BG_COLOR)
window.resizable(False,False)

timer_label = Label(text="Timer", fg=TEXT_COLOR, bg=BG_COLOR, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=300, height=301, bg=BG_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(160, 151, image=tomato_img)
timer_clock = canvas.create_text(160, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 20, "normal"), command=start_timer)
start_button.grid(column=0, row=2)

progress_text = Label(text="", fg=GREEN, bg=BG_COLOR, font=(FONT_NAME, 25, "normal"))
progress_text.grid(column=1, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 20, "normal"), command=reset_app)
reset_button.grid(column=2, row=2)

window.mainloop()