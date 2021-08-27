'''
import tkinter
from tkinter import *
import time

local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
root = Tk()
root.title("pictrue")
text_lable = Label(root,
            text = local_time,
            justify = LEFT,
            padx = 10,
            pady = 10)
text_lable.pack(side = LEFT)

photo = PhotoImage(file = '2570.png_300.png')
imageLabel = Label(root, image = photo)
imageLabel.pack(side=RIGHT)

while(True):
    time.sleep(1)
    root.update()
    root.after(1000)  
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    #print(local_time)
    text_lable = Label(root,
            text = local_time,
            justify = LEFT,
            padx = 10,
            pady = 10)

root.mainloop()

'''
import tkinter as tk
import time
from tkinter import *

class Questions(tk.Tk):
    def __init__(self, *args, **kw):
        super().__init__()
        #self.wm_title(self.local_time)
        self.wm_title('time:')
        self.configure(background = 'blue')
        self.wm_minsize(320, 320)
        self.wm_maxsize(650, 650)
        self.resizable(width = True, height = True)
        photo = PhotoImage(file = '2570.png_300.png')
        imageLabel = Label(self, image = photo)
        imageLabel.pack(side=TOP)

        self.run()
        self.refresh_data()
        self.mainloop()

    def refresh_data(self):
        self.local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.wm_title(self.local_time)
        self.after(1000, self.refresh_data)

    def run(self):
        pass

if __name__ == '__main__':
    question = Questions()
