from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE
clicked_start_button = False

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global reps, clicked_start_button
    canvas.itemconfig(timer_text, text=f"00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    reps = 0
    clicked_start_button = False
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global clicked_start_button
    if clicked_start_button:
        pass
    else:
        clicked_start_button = True
        global reps
        reps += 1

        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            label.config(fg=RED)
            count_down(long_break_sec, "Long break")
        elif reps % 2 == 1:
            label.config(fg=GREEN)
            count_down(work_sec, "Work Time")
        else:
            label.config(fg=PINK)
            count_down(short_break_sec, "Short Break")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, mode):
    label.config(text=mode)
    sec = count % 60
    mins = count // 60
    if count > 0:
        global timer
        if mins < 10:
            if sec < 10:
                canvas.itemconfig(timer_text, text=f"0{mins}:0{sec}")
            else:
                canvas.itemconfig(timer_text, text=f"0{mins}:{sec}")
        elif mins >= 10:
            if sec < 10:
                canvas.itemconfig(timer_text, text=f"{mins}:0{sec}")
            else:
                canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
        timer = window.after(1000, count_down, count - 1, mode)
    else:
        marks = ""
        for _ in range(reps):
            marks += "✅"
        checkmark.config(text=marks)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=430, height=450)
window.config(bg=YELLOW)
window.config(padx=100, pady=30)


canvas = Canvas(width=250, height=250, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(126, 136, image=tomato_img)
timer_text = canvas.create_text(127, 155, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), foreground=GREEN)
label.grid(column=1, row=0)


start = Button(text="start", command=start_timer)
start.grid(column=0, row=2)

resetb = Button(text="Reset", command=reset)
resetb.grid(column=2, row=2)

checkmark = Label(text="", fg="blue")
checkmark.grid(column=1, row=3)

window.mainloop()