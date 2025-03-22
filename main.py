import time
from tkinter import *
from tkinter import messagebox



root = Tk()

root.geometry ("300x300")

root.title ("Geri Sayım")

root.config(bg="black")

hour=StringVar()
minute=StringVar()
second=StringVar()


hour.set("00")
minute.set("00")
second.set("00")

hourEntry= Entry(root, width=5 , font=("Arial",18,"bold"),
                  textvariable=hour,justify="center", bd=5,fg="limegreen",bg="yellow")
hourEntry.place (x=45,y=20)


minuteEntry= Entry(root, width=5 , font=("Arial",18,"bold"),
                  textvariable=minute,justify="center", bd=5,fg="limegreen",bg="yellow")
minuteEntry.place (x=117,y=20)


seckondEntry= Entry(root, width=5 , font=("Arial",18,"bold"),
                  textvariable=second,justify="center", bd=5,fg="limegreen",bg="yellow")
seckondEntry.place (x=190,y=20)

running=False


def submit():
    global running
    if running:
        return
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right Value")
        return

    running =True


    while temp > 0 and running:
            mins,secs = divmod(temp,60)
            hours = 0
            if mins >= 60:
                hours, mins = divmod(mins, 60)



            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            temp -= 1

            root.update()
            time.sleep(1)
    if(temp == 0) :
            messagebox.showinfo(("Time's up"))
    running = False


def stop_timer():
    global running
    running = False






btn =Button(root, text='Start Countdown',font=("Arial",14,"bold"),justify="center",fg="limegreen",
            bg="orange",relief="raised", bd='5',width=15, height=2,
            command = submit)

btn.place (x =55,y = 120)



btn_stop = Button(root, text=' Stop ', font=("Arial", 14, "bold"), justify="center", fg="limegreen",
                  bg="red", relief="raised", bd='5', width=10, height=1,
                  command=stop_timer)
btn_stop.place(x=85, y=190)




root.mainloop()



