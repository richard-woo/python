import tkinter as tk
import pickle
import tkinter.messagebox
from PIL import Image, ImageTk

# 设置窗口---最开始的母体窗口
window = tk.Tk()  # 建立一个窗口
window.title('欢迎登录')
window.geometry('450x300')  # 窗口大小为300x200

# 画布
canvas = tk.Canvas(window, height=200, width=900)
# 加载图片
im = Image.open("images/01.png")
image_file = ImageTk.PhotoImage(im)
# image_file = tk.PhotoImage(file='images/01.gif')
image = canvas.create_image(100, 40, anchor='nw', image=image_file)
canvas.pack(side='top')

# 两个文字标签，用户名和密码两个部分
tk.Label(window, text='用户名').place(x=100, y=150)
tk.Label(window, text='密  码').place(x=100, y=190)

var_usr_name = tk.StringVar()  # 讲文本框的内容，定义为字符串类型
var_usr_name.set('amoxiang@163.com')  # 设置默认值
var_usr_pwd = tk.StringVar()

# 第一个输入框-用来输入用户名的。
# textvariable 获取文本框的内容
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)
# 第二个输入框-用来输入密码的。
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(
                title='欢迎光临', message=usr_name + '：请进入个人首页，查看最新资讯')
        else:
            tk.messagebox.showinfo(message='错误提示：密码不对，请重试')
    else:
        is_sign_up = tk.messagebox.askyesno('提示', '你还没有注册，请先注册')
        print(is_sign_up)
        if is_sign_up:
            usr_sign_up()


# 注册按钮
def usr_sign_up():
    def sign_to_Mofan_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        # 上面是获取数据，下面是查看一下是否重复注册过
        with open('usrs_info.pickle', 'rb') as usr_file:
            exist_usr_info = pickle.load(usr_file)
            if np != npf:
                tk.messagebox.showerror('错误提示', '密码和确认密码必须一样')
            elif nn in exist_usr_info:
                tk.messagebox.showerror('错误提示', '用户名早就注册了！')
            else:
                exist_usr_info[nn] = np
                with open('usrs_info.pickle', 'wb') as usr_file:
                    pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo('欢迎', '你已经成功注册了')
                window_sign_up.destroy()

    # 点击注册之后，会弹出这个窗口界面。
    window_sign_up = tk.Toplevel(window)
    window_sign_up.title('欢迎注册')
    window_sign_up.geometry('360x200')  # 中间是x，而不是*号

    # 用户名框--这里输入用户名框。
    new_name = tk.StringVar()
    new_name.set('amoxiang@163.com')  # 设置的是默认值
    tk.Label(window_sign_up, text='用户名').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=100, y=10)

    # 新密码框--这里输入注册时候的密码
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='密  码').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=100, y=50)

    # 密码确认框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='确认密码').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(
        window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=100, y=90)

    btn_confirm_sign_up = tk.Button(
        window_sign_up, text=' 注  册 ', command=sign_to_Mofan_Python)
    btn_confirm_sign_up.place(x=120, y=130)


# 创建注册和登录按钮
btn_login = tk.Button(window, text=' 登  录 ', command=usr_login)
btn_login.place(x=150, y=230)  # 用place来处理按钮的位置信息。
btn_sign_up = tk.Button(window, text=' 注  册 ', command=usr_sign_up)
btn_sign_up.place(x=250, y=230)

window.mainloop()