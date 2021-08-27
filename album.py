#一个电子相册
import os
import sys
import threading
import tkinter as tk
import time
from PIL import ImageTk, Image
import pygame
from mutagen.mp3 import MP3

def playmusic():
    Path = r'music\\'
    try:
        list1 = os.listdir(Path) #获取指定路径下的所有mp3文件
        for x in list1:
            if not (x.endswith('.mp3')):
                list1.remove(x)

        list2 = []
        for i in list1:
            s = os.path.join(Path, i) #对路径与文件进行拼接
            list2.append(s)

        while True:
            for n in list2:
                #获取每一首歌的时长
                path = n
                audio = MP3(n)
                pygame.mixer.init() #初始化所引入的模块
                pygame.mixer.music.load(path) #load music , music could be ogg, mp3 format
                pygame.mixer.music.play() #paly music which is loaded
                time.sleep(int(audio.info.length)) #获取每一首歌的时长，使程序存活的时长等于歌曲时长

    except Exception as e:
        print("Exception0: %s" % e)


resolution = (640, 480) #分辨率
Path = r'photo\\' #相册路径
Interval = 5 #播放间隔，单位s
Index = 0 #当前照片计数
title = "电子相册"

def getfiles():
    files = os.listdir(Path)
    for x in files:
        if not (x.endswith('.jpg') 
            or x.endswith('.JPG') 
            or x.endswith('.png')
            or x.endswith('.jpeg')
            or x.endswith('.JPEG')):
            files.remove(x)
    return files

files = getfiles()
print(files)
scaler = Image.ANTIALIAS #设定ANTIALIAS， 即抗锯齿
root = tk.Tk()
root.title(title)

img_in = Image.open(Path + files[0]) #load first image
w, h = img_in.size #get image size
size_new = (int(w * resolution[1] / h), resolution[1])
img_out = img_in.resize(size_new, scaler) #重新设置大小
img = ImageTk.PhotoImage(img_out) #用PhotoImage打开图片
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback(e):
    try:
        global Index
        for i, x in enumerate(files):
            #判断文件是否存在
            if not os.path.isfile(Path + '%s' % x):
                break

            if i != Index:
                continue

            print('手动处理图片', x, Index)
            img_in = Image.open(Path + '%s' % x)
            print(img_in)
            w, h = img_in.size
            size_new = (int(w * resolution[1] / h), resolution[1])
            img_out = img_in.resize(size_new, scaler)
            img2 = ImageTk.PhotoImage(img_out)
            panel.configure(image=img2)
            panel.image = img2
            Index += 1
            if Index >= len(files):
                Index = 0
            break

    except Exception as e:
        print("Exception1: %s" % e)
        sys.exit(1)

root.bind("<Button-1>", callback) #点击窗口切换下一张图片

def image_change():
    try:
        global Index
        time.sleep(3)
        while True:
            for i, x in enumerate(files):
                #判断图片是否存在
                if not os.path.isfile(Path + '%s' % x):
                    break
                if i != Index: #跳过已播放的图片
                    continue

                print('自动处理图片', i, Index)
                img_in = Image.open(Path + '%s' % x)
                w, h = img_in.size
                size_new = (int(w * resolution[1] / h), resolution[1])
                img_out = img_in.resize(size_new, scaler)
                img2 = ImageTk.PhotoImage(img_out)
                panel.configure(image=img2)
                panel.image = img2
                Index += 1
                if Index >= len(files):
                    Index = 0
                time.sleep(Interval)

    except Exception as e:
        print("Exception2: %s" % e)
        sys.exit(1)                

m = threading.Thread(target=playmusic) #创建音乐播放线程
t = threading.Thread(target=image_change)

m.setDaemon(True)
m.start()
t.start()
root.mainloop()