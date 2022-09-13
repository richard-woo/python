from tkinter import *
import tkinter as tk

window = Tk()
window.title("stock calculator!")
window.geometry('350x200') 

lbl = Label(window, text="成本")
lbl.grid(column=0, row=0)
cost_txt = Entry(window, width = 10)
cost_txt.grid(column = 1, row = 0)

lbl_n = Label(window, text="    数量")
lbl_n.grid(column=2, row=0)
num_txt = Entry(window, width = 10)
num_txt.grid(column = 3, row = 0)

lbl_p = Label(window, text="现价")
lbl_p.grid(column=0, row=1)
price_txt = Entry(window, width = 10)
price_txt.grid(column = 1, row = 1)

lbl_shou = Label(window, text="     手")
lbl_shou.grid(column=2, row=1)
shou_txt = Entry(window, width = 10)
shou_txt.grid(column = 3, row = 1)

lbl_res = Label(window, text="摊薄:")
lbl_res.grid(column=0, row=3)
lbl_res_show = Label(window, text=" ")
lbl_res_show.grid(column=1, row=3)

lbl_res_per = Label(window, text="相对现价:")
lbl_res_per.grid(column=0, row=4)
lbl_res_per_show = Label(window, text=" ")
lbl_res_per_show.grid(column=1, row=4)

def clicked():
    res_cost = cost_txt.get()
    nums = num_txt.get()
    res_price = price_txt.get()
    shou = shou_txt.get()
    #print('out put ' + res_cost + res_price)
    res = float(res_cost) * float(nums) + float(res_price) * float(shou) * 100
    res = res / (float(nums) + float(shou) * 100)
    per = (res - float(res_price)) / float(res_price) * 100
    res = round(res, 3)
    per = round(per, 3)
    lbl_res_show.configure(text = str(res))
    lbl_res_show.grid(column=1, row=3)
    lbl_res_per_show.configure(text = str(per)+'%')
    lbl_res_per_show.grid(column=1, row=4)
    #txt.destroy()
    #btn.grid_forget()
    
btn = Button(window, text = "提交", command = clicked)
btn.grid(column = 15, row = 15)
window.mainloop()