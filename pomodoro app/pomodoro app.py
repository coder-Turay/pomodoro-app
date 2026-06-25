import tkinter as tk
from PIL import Image,ImageTk
import time 
import winsound
window=tk.Tk()
window.geometry("1535x800")
window.title("Pomodoro app")
image = Image.open(
    r"C:\Users\user\Desktop\Portfoliom\pomodoro app\image.jpeg"
)
image=image.resize((1535,800))                     
photo=ImageTk.PhotoImage(image)


label_bg=tk.Label(window,image=photo)
label_bg.place(x=0,y=0)

study=tk.Label(window,text="Study effectively!",font=("Times new roman",50,"bold italic"))


minutes=25
seconds=0
label=tk.Label(window,text="25:00",width=8,height=3,font=("Arial",25,"bold"))

running=False
def set_time(x):
    global running,minutes,seconds
    running = False
    button_start.config(text="Start")
    minutes = x
    seconds = 0
    if minutes == 5:
        label.config(text="05:00")
    else:
          label.config(text=str(minutes)+":00")


def click():
    global running
    if running == False:
        button_start.config(text="Pause")
        running = True
        timer()
    else:
        running = False
        button_start.config(text="Start")
        
def timer():
    global minutes
    global seconds
    global running
    if running == False:
        return
    if minutes == 0 and seconds == 0:
        running = False
        button_start.config(text="Start")
        winsound.PlaySound(r"C:\Users\user\Desktop\Portfoliom\pomodoro app\Bell.wav",winsound.SND_FILENAME )
        return
    
 
    
    if seconds == 0:
        minutes-=1
        seconds = 59
    else:
        seconds-=1
    if 0<=seconds<=9:
        if 0<=minutes<=9:
             label.config(text="0"+str(minutes)+":"+"0"+str(seconds))
        else:
            label.config(text=str(minutes)+":"+"0"+str(seconds))

    else:
        if 0<=minutes<=9:
            label.config(text="0"+str(minutes)+":"+str(seconds))
        else:
            label.config(text=str(minutes)+":"+str(seconds))
    window.after(1000,timer)
   



    

button_start=tk.Button(window,text='Start',font=("Arial", 12, "bold"),width=10,height=3,command=lambda: click())

button_study=tk.Button(window,text="Study",font=("Arial", 12, "bold"),width=10,height=3,command=lambda: set_time(25))
button_longbreak=tk.Button(window,text="Long break",font=("Arial", 12, "bold"),width=10,height=3,command=lambda: set_time(10))

button_shortbreak=tk.Button(window,text="Short break",font=("Arial", 12, "bold"),width=10,height=3,command=lambda: set_time(5))

study.place(relx=0.5, rely=0.08, anchor="center")

button_study.place(relx=0.38, rely=0.22, anchor="center")
button_shortbreak.place(relx=0.50, rely=0.22, anchor="center")
button_longbreak.place(relx=0.62, rely=0.22, anchor="center")

label.place(relx=0.5, rely=0.45, anchor="center")

button_start.place(relx=0.5, rely=0.65, anchor="center")

window.mainloop()