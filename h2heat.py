import tkinter as tk
from tkinter import messagebox
import random
screen = tk.Tk()
screen.title("game screen")
screen.geometry("1400x800")
screen.config(bg="white")

number = random.randint(1,20)

label1=tk.Label(screen,text="celcius to farrenheight converter",fg="black",font=("arial",70))
label1.place(x=0,y=20)

label2=tk.Label(screen,text="enter temp",fg="black",font=("arial",20))
label2.place(x=300,y=300)

entry=tk.Entry(screen,width=50)
entry.place(x=530,y=310)

label3=tk.Label(screen,text="temperature in farrenheight: ",fg="black",font=("arial",20))
label3.place(x=500,y=550)
label4=tk.Label(screen,fg="black",font=("arial",20))
label4.place(x=850,y=550)


def ok():
  try:
    f = int(entry.get())*9/5+32
    label4.config(text=f,fg="black")
  except:
    label4.config(text="invalid",fg="red")
   

button=tk.Button(screen,text="convert",border=30,command=ok)
button.place(x=600,y=400)



















screen.mainloop()