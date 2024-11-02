from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # Duration of work session in minutes
SHORT_BREAK_MIN = 5  # Duration of short break in minutes
LONG_BREAK_MIN = 20  # Duration of long break in minutes
TOTAL_CYCLES = 4  # Total cycles for a complete Pomodoro session
reps = 0  # Tracks the current cycle number
timer = None  # Timer reference for cancellation


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer, clears the check marks, and resets UI to initial state."""
    global reps, timer
    reps = 0
    # Cancel any active timer
    if timer:
        window.after_cancel(timer)
        timer = None
    # Reset timer display and indicators
    canvas.itemconfig(timer_text, text="00:00")
    indicator.config(text="Timer", bg=YELLOW, fg=GREEN)
    window.config(bg=YELLOW)
    canvas.config(bg=YELLOW)
    check_mark.config(text="")
    # Re-enable start button
    start_button.config(state="normal")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and alternates between work and break sessions up to the total cycles limit."""
    global reps, timer

    # Prevent multiple concurrent timers by disabling start button
    start_button.config(state="disabled")

    # Increment cycle count
    reps += 1

    # Check if Pomodoro session is complete after 4 cycles
    if reps > TOTAL_CYCLES * 2:
        indicator.config(text="Session Complete!", bg=YELLOW, fg=GREEN)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        check_mark.config(bg=YELLOW)
        reset_timer()
        return

    # Configure for work session
    if reps % 2 == 1:
        indicator.config(text="Work", bg=YELLOW, fg=GREEN)
        window.config(bg=YELLOW)
        canvas.config(bg=YELLOW)
        check_mark.config(bg=YELLOW)
        countdown(WORK_MIN * 60)

    # Configure for break session
    elif reps % 2 == 0:
        window.config(bg=PINK)
        canvas.config(bg=PINK)
        check_mark.config(bg=PINK)
        indicator.config(text="Break", fg=RED, bg=PINK)
        if reps == TOTAL_CYCLES * 2:
            # Last cycle uses long break
            countdown(LONG_BREAK_MIN * 60)
        else:
            countdown(SHORT_BREAK_MIN * 60)

        # Update check marks to show completed work sessions
        check_marks = "✓" * (reps // 2)
        check_mark.config(text=check_marks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    """Handles the countdown timer and updates the UI to display remaining time."""
    minutes = count // 60
    seconds = count % 60
    formatted_time = f"{minutes:02}:{seconds:02}"
    canvas.itemconfig(timer_text, text=formatted_time)

    # Continue countdown if time remains
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        # Start next timer after countdown reaches zero
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

# Main application window
window = Tk()
window.title("Pomodoro Timer")
window.config(bg=YELLOW, padx=100, pady=50)

# Work and Break indicator label
indicator = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
indicator.grid(column=2, row=1)

# Display tomato image and add text on top of it
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=tomato_img)
timer_text = canvas.create_text(110, 130, text="00:00",fill="white" ,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start button to initiate timer
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

# Label to display check marks for completed work sessions
check_mark = Label(text="", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
check_mark.grid(column=2, row=4)

# Reset button to reset the timer and clear progress
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

window.mainloop()

#
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 5
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
#
# # ---------------------------- TIMER RESET ------------------------------- #
# def reset_timer():
#     indicator.config(text="Timer")
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text,text = "00:00")
#     window.config(bg=YELLOW)
#     canvas.config(bg=YELLOW)
#     check_mark.config(bg=YELLOW)
#     new_str= ""
#     check_mark.config(text=new_str)
#
# # ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_timer():
#     global reps
#     reps += 1
#     if reps % 2 == 1:
#         indicator.config(text="Work",bg=YELLOW,fg=GREEN)
#         window.config(bg=YELLOW)
#         canvas.config(bg=YELLOW)
#         check_mark.config(bg=YELLOW)
#         countdown(WORK_MIN * 60)
#
#     elif reps % 2 == 0 and reps!=8:
#         indicator.config(text="Break", fg=RED,bg=PINK)
#         check_mark.config(bg=PINK)
#         canvas.config(bg=PINK)
#         window.config(bg=PINK)
#         countdown((SHORT_BREAK_MIN * 60))
#         check_ = "✓"
#         for i in range (0,int(reps/2)+1):
#             new_string = check_*i
#             check_mark.config(text=new_string)
#     else:
#         indicator.config(text="Break", fg=RED,bg=PINK)
#         window.config(bg=PINK)
#         check_mark.config(bg=PINK)
#         canvas.config(bg=PINK)
#         check_ = "✓"
#         for i in range(0, int(reps / 2) + 1):
#             new_string = check_ * i
#             check_mark.config(text=new_string)
#         countdown(LONG_BREAK_MIN * 60)
#
#
# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def countdown(count):
#     minutes = count // 60
#     seconds = count % 60
#     if seconds<10:
#         seconds=f"0{seconds}"
#     # canvas.itemconfig(timer_text,text =f"{minutes:02}:{seconds:02}")
#     canvas.itemconfig(timer_text,text =f"{minutes}:{seconds}")
#     if count>0:
#         global timer
#         timer = window.after(10,countdown,count-1)
#     else:
#         start_timer()
# # ---------------------------- UI SETUP ------------------------------- #
#
# #main window
# window = Tk()
# window.title("Pomodoro Timer")
# window.config(bg=YELLOW,padx=100,pady=50)
#
# #Work and Break indicator label
# indicator = Label(text="Timer",font=(FONT_NAME,50,"bold"),bg=YELLOW,fg=GREEN)
# indicator.grid(column = 2,row = 1)
#
# #display tomato image and add text on top of it
# canvas = Canvas(width=220,height=224)
# canvas.config(bg=YELLOW,highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(110,112,image = tomato_img)
# timer_text = canvas.create_text(110,130,text="00:00",font=(FONT_NAME,35,"bold"))
# canvas.grid(column = 2,row=2)
#
# # start button
# start_button = Button(text="Start",command=start_timer)
# start_button.grid(column=1,row=3)
#
# # check label
# check_string =""
# check_mark = Label(text=check_string,fg=GREEN,font=(FONT_NAME,25,"bold"),bg=YELLOW)
# check_mark.grid(column = 2,row =4)
#
# # reset button
# start_button = Button(text="Reset",command=reset_timer)
# start_button.grid(column=3,row=3)
#
#
# window.mainloop()