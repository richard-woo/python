from tkinter import *
import tkinter as tk

window = Tk()
window.title("hello word!")
window.geometry('350x200') 

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width = 10)
txt.grid(column = 1, row = 0)

def clicked():
    res = "Welcome to new world, " + txt.get()
    lbl.configure(text = res)
    txt.destroy()
    btn.grid_forget()
    
btn = Button(window, text = "submit", command = clicked)
btn.grid(column = 2, row = 0)
window.mainloop()