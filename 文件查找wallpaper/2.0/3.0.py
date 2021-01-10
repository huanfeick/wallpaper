# -*- coding:utf-8 -*-

"""
时间:2020年10月01日
作者:幻非
"""

import os
import json
import pyperclip
import tkinter
import tkinter.messagebox
import random
from tkinter import *


wallpaper_path = "E:\\Steam\\steamapps\\workshop\\content\\431960"  #wallpaper保存视频位置
file_type = ".mp4"  #查找的文件类型
video_list = []   #全部视频地址列表
list_history = []   #历史播放的视频名称列表
dict = {}


player = tkinter.Tk()#窗口
player.title("wallpaper engine查找")
mw, mh = player.maxsize()
player.geometry('360x380+%d+%d'%((mw-500)/2,(mh-300)/2)) #窗口居中
player.resizable(0,0) #锁定窗口大小
player.wm_attributes('-topmost',1) #窗口置顶

def video_play(path):#打开视频
	class Video(object):
	    def __init__(self,path):
	        self.path = path
	    def play(self):
	        from os import startfile
	        startfile(self.path)
	class Movie_MP4(Video):
	    type = 'MP4'
	movie = Movie_MP4(path)
	movie.play()

def search_file(path, str):  #获取路径下所有的视频路径
    # 首先先找到当前目录下的所有文件
    for file in os.listdir(path):  # os.listdir(path) 是当前这个path路径下的所有文件的列表
        this_path = os.path.join(path, file)
        if os.path.isfile(this_path):  # 判断这个路径对应的是目录还是文件，是文件就走下去
            if str in file:
                video_list.append(this_path)
        else:   # 不是就再次执行这个函数，递归下去
            search_file(this_path, str)  # 递归下去
    return(video_list)


path_list = search_file(wallpaper_path,file_type)   #全部视频地址列表
rand = random.sample(range(1, len(path_list)), len(path_list) - 1)      #将全部视频地址序列打散
i = 1
#print(rand)


def random_video():
    global i
    video_data_title = os.path.basename(os.path.splitext(path_list[rand[i]])[0])    #随机播放视频的名称
    dict[video_data_title] = path_list[rand[i]]     #字典
    #print(path_list[rand[i]])
    video_play(path_list[rand[i]])      #打开视频

    list_history.append(video_data_title)
    listbox_history.delete(0, END)
    for item in list_history:
        listbox_history.insert(0, item)

    i = i + 1

def buttonList(event):
    video_name = listbox_history.get(listbox_history.curselection())    #获取点击的视频名称
    video_play(dict[video_name])        #查找字典播放视频

btn_Random_video = tkinter.Button(player,text = "随机视频",height=4,width=16,command = random_video)#随机视频
btn_Random_video.place(x=40,y=30)

# btn_title = tkinter.Button(player,text = "复制标题",height=4,width=16,command = "list_title")#列出标题并复制到剪切板
# btn_title.place(x=40, y=140)

listbox_history = tkinter.Listbox(player,width=20,height=20,)
listbox_history.bind('<Double-Button-1>',buttonList)     #双击事件
listbox_history.place(x=200,y=10)


player.mainloop()
