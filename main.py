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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps=0
    canvas.itemconfig(canvas_text_item,text="00:00")
    windows.after_cancel(timer)
    label.config(text="Timer",foreground=GREEN)
    check_var.set("")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    if(reps%2==0):
        windows.attributes("-topmost",0)
        label.config(text="Work",foreground=GREEN)
        countDown(5)#WORK_MIN*60)
    elif(reps%8==7):
        windows.attributes("-topmost",1)
        label.config(text="Break",foreground=RED)
        countDown(4)#LONG_BREAK_MIN*60)
    else:
        windows.attributes("-topmost",1)
        label.config(text="Break",foreground=PINK)
        countDown(3)#SHORT_BREAK_MIN*60)
    reps=reps+1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countDown(count):
    global reps
    min=math.floor(count/60)
    sec=count-min*60
    canvas.itemconfig(canvas_text_item,text=f"{min:02}:{sec:02}")
    if(count>0):
        global timer
        timer=windows.after(1000,countDown,count-1)
    else:
        # print(reps)
        if((reps-1)%2==0):
            # print(check_var)
            check_var.set(f"{check_var.get()}✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.config(background=YELLOW)
windows.title("Pomodoro")
windows.config(padx=120,pady=80)

#label
label=Label(text="Timer")
label.config(font=(FONT_NAME,40,"bold"),foreground=GREEN,background=YELLOW)
# label.grid(row=0,column=1)
label.grid(row=0,column=1)


canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas_text_item=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#check mark
check_var=StringVar()
check_mark=Label(textvariable=check_var)
check_mark.config(foreground=GREEN,pady=30,background=YELLOW)
check_mark.grid(row=3,column=1)

#button
button1=Button(text="Start",highlightthickness=0,command=start_timer)
button1.grid(row=2,column=0)

button2=Button(text="Reset",highlightthickness=0,command=reset_timer)
button2.grid(row=2,column=2)



windows.mainloop()
