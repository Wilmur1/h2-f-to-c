import tkinter as tk  
from tkinter import messagebox
from tkinter.ttk import Combobox
screen = tk.Tk()
screen.geometry("1700x900")
label=tk.Label(screen,text="mathematical table",fg="black",font=("arial",100))
label.place(x=400,y=20)

label=tk.Label(screen,text="number and range",fg="black",font=("arial",20))
label.place(x=300,y=300)

button=tk.Button(screen,text="generate",border=10,font=("arial",20,"bold"))
button.place(x=900,y=280)

dropdown = Combobox(screen,values=[1,2,3,4,5],state="readonly")
dropdown.set("pick a number")
dropdown.place(x=550,y=310)
radio = tk.IntVar()
radio1=tk.Radiobutton(screen,text="10",variable=radio,value=10,cursor="hand2")
radio1.place(x=100,y=200)

radio2=tk.Radiobutton(screen,text="20",variable=radio,value=20,cursor="hand2")
radio2.place(x=100,y=220)

radio3=tk.Radiobutton(screen,text="30",variable=radio,value=30,cursor="hand2")
radio3.place(x=100,y=240)

radio.set(20)


label=tk.Label(screen,text=dropdown.get()*radio.get(),fg="black",bg="red",font=("arial",100))
label.place(x=700,y=100)


                                                                                                                    










screen.mainloop()