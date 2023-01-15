from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

#icon
image_icon=PhotoImage(file="")
root.iconphoto(False,image_icon)

#logo
logo=PhotoImage(file="")
Label(root,image=logo, bg="#2f4155").place(x=10,y=0)

Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font="arial 25 bold").place(x=100,y=20)

#fist Frame
f=Frame(root,bd="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lb1=Label(f,bg="black")
lb1.place(x=40,y=10)

#second Frame
frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20", bg="white",fg="black",relief=GROOVE, wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)






root.mainloop()

 