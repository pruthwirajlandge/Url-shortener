import pyshorteners
from tkinter import *

win=Tk()
win.geometry("1000x500")
win.configure(bg="pink")
#Buttonb Fuction
def short():
    url=entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)

    entry2.insert(END,s)
# label for user entering URL
Label(win,text="Enter your url link",font="impack 17 bold",bg="black",fg="white").pack(fill="x")

#Entry Box
entry1= Entry(win,font="30",bd=3,width=60)
entry1.pack(pady=30)

#Button
Button(win,text="Click Here",font="impack 12 bold",bg="blue",fg="white",command=short).pack()

#entry
entry2=Entry(win,font="impack 16 bold",bg="pink",width=24,bd=0)
entry2.pack(pady=30)
mainloop()

