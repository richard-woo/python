from tkinter import *
import tkinter as tk

window = Tk()
window.title("hello word!")
window.geometry('350x200') 

lbl = Label(window, text="成本")
lbl.grid(column=0, row=0)
cost_txt = Entry(window, width = 10)
cost_txt.grid(column = 1, row = 0)

lbl_p = Label(window, text="现价")
lbl_p.grid(column=0, row=1)
price_txt = Entry(window, width = 10)
price_txt.grid(column = 1, row = 1)

lbl_res = Label(window, text="结果")
lbl_res.grid(column=0, row=2)
res_txt = Entry(window, width = 10)
res_txt.grid(column = 1, row = 1)


def clicked():
    res = "Welcome to new world, " + cost_txt.get()
    lbl_res.configure(text = res)
    lbl_res.grid(column=0, row=5)
    #txt.destroy()
    btn.grid_forget()
    
btn = Button(window, text = "submit", command = clicked)
btn.grid(column = 5, row = 0)
window.mainloop()