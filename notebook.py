from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

filename = ""


def author():
    showinfo(title="作者", message="Python")


def power():
    showinfo(title="版权信息", message="课堂练习")


def mynew():
    global top, filename, textPad
    top.title("未命名文件")
    filename = None
    textPad.delete(1.0, END)


def myopen():
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        top.title("记事本" + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def mysave():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        mysaveas()


def mysaveas():
    global filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    top.title("记事本 " + os.path.basename(f))


def cut():
    global textPad
    textPad.event_generate("<<Cut>>")


def copy():
    global textPad
    textPad.event_generate("<<Copy>>")


def paste():
    global textPad
    textPad.event_generate("<<Paste>>")


def undo():
    global textPad
    textPad.event_generate("<<Undo>>")


def redo():
    global textPad
    textPad.event_generate("<<Redo>>")


def select_all():
    global textPad
    # textPad.event_generate("<<Cut>>")
    textPad.tag_add("sel", "1.0", "end")


def find():
    t = Toplevel(top)
    t.title("查找")
    t.geometry("260x60+200+250")
    t.transient(top)
    Label(t, text="查找：").grid(row=0, column=0, sticky="e")
    v = StringVar()
    e = Entry(t, width=20, textvariable=v)
    e.grid(row=0, column=1, padx=2, pady=2, sticky="we")
    e.focus_set()
    c = IntVar()
    Checkbutton(t, text="不区分大小写", variable=c).grid(row=1, column=1, sticky='e')
    Button(t, text="查找所有", command=lambda: search(v.get(), c.get(),
                                                  textPad, t, e)).grid(row=0, column=2, sticky="e" + "w", padx=2,
                                                                       pady=2)

    def close_search():
        textPad.tag_remove("match", "1.0", END)
        t.destroy()

    t.protocol("WM_DELETE_WINDOW", close_search)


def mypopup(event):
    # global editmenu
    editmenu.tk_popup(event.x_root, event.y_root)


def search(needle, cssnstv, textPad, t, e):
    textPad.tag_remove("match", "1.0", END)
    count = 0
    if needle:
        pos = "1.0"
        while True:
            pos = textPad.search(needle, pos, nocase=cssnstv, stopindex=END)
            if not pos:
                break
            lastpos = pos + str(len(needle))
            textPad.tag_add("match", pos, lastpos)
            count += 1
            pos = lastpos
        textPad.tag_config('match', fg='yellow', bg="green")
        e.focus_set()
        t.title(str(count) + "个被匹配")


top = Tk()
top.title("记事本")
top.geometry("600x400+100+50")

menubar = Menu(top)

# 文件功能
filemenu = Menu(top)
filemenu.add_command(label="新建", accelerator="Ctrl+N", command=mynew)
filemenu.add_command(label="打开", accelerator="Ctrl+O", command=myopen)
filemenu.add_command(label="保存", accelerator="Ctrl+S", command=mysave)
filemenu.add_command(label="另存为", accelerator="Ctrl+shift+s", command=mysaveas)
menubar.add_cascade(label="文件", menu=filemenu)

# 编辑功能
editmenu = Menu(top)
editmenu.add_command(label="撤销", accelerator="Ctrl+Z", command=undo)
editmenu.add_command(label="重做", accelerator="Ctrl+Y", command=redo)
editmenu.add_separator()
editmenu.add_command(label="剪切", accelerator="Ctrl+X", command=cut)
editmenu.add_command(label="复制", accelerator="Ctrl+C", command=copy)
editmenu.add_command(label="粘贴", accelerator="Ctrl+V", command=paste)
editmenu.add_separator()
editmenu.add_command(label="查找", accelerator="Ctrl+F", command=find)
editmenu.add_command(label="全选", accelerator="Ctrl+A", command=select_all)
menubar.add_cascade(label="编辑", menu=editmenu)

# 关于 功能
aboutmenu = Menu(top)
aboutmenu.add_command(label="作者", command=author)
aboutmenu.add_command(label="版权", command=power)
menubar.add_cascade(label="关于", menu=aboutmenu)

top['menu'] = menubar

# shortcutbar = Frame(top, height=25, bg='light sea green')
# shortcutbar.pack(expand=NO, fill=X)
# Inlabe = Label(top, width=2, bg='antique white')
# Inlabe.pack(side=LEFT, anchor='nw', fill=Y)

textPad = Text(top, undo=True)
textPad.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

# 热键绑定
textPad.bind("<Control-N>", mynew)
textPad.bind("<Control-n>", mynew)
textPad.bind("<Control-O>", myopen)
textPad.bind("<Control-o>", myopen)
textPad.bind("<Control-S>", mysave)
textPad.bind("<Control-s>", mysave)
textPad.bind("<Control-A>", select_all)
textPad.bind("<Control-a>", select_all)
textPad.bind("<Control-F>", find)
textPad.bind("<Control-f>", find)

textPad.bind("<Button-3>", mypopup)
top.mainloop()