from cProfile import *
from tkinter import *


window = Tk()
window.title("Calculator")
button = Button(window,text="ok",width=30,height=30,bg="green",fg="black" )
label=Label(window,text="welcome")
label.pack()
button.pack()
window.mainloop()


