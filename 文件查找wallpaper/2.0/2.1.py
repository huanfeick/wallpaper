import os
import json
import pyperclip
import tkinter
import tkinter.messagebox
import random

wallpaper_path = "E:\\Steam\\steamapps\\workshop\\content\\431960"  #wallpaper保存视频位置
file_type = ".mp4"  #查找的文件类型
list = []
file_title = ""

player = tkinter.Tk()#窗口
player.title("wallpaper engine查找")
mw, mh = player.maxsize()
player.geometry('150x180+%d+%d'%((mw-500)/2,(mh-300)/2)) #窗口居中
player.resizable(0,0) #锁定窗口大小
player.wm_attributes('-topmost',1) #窗口置顶

def videoplay(path):#打开视频
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
                list.append(this_path)
        else:   # 不是就再次执行这个函数，递归下去
            search_file(this_path, str)  # 递归下去
    return(list)

def search_title(path): #查出该视频的wallpaper标题名称
    way = os.path.exists(path + "\\project.json")
    if way == True:
        jsonfile = open(path + "\\project.json",encoding='utf-8')
        res = jsonfile.read()
        data = json.loads(res)
        return(data["title"])
        #pyperclip.copy(data["title"])
    else:
        return(None)

def Play_video():
    global file_title
    rand = random.randint(1, len(wallpaper_path_list))
    videoplay(wallpaper_path_list[rand])
    file_title = wallpaper_path_list[rand]
    btn_title.place(x=45, y=100)


def list_title():
    get_title = search_title(os.path.dirname(file_title))
    if get_title == None:
        title = "该视频可能不属于wallpaper" + '\r' + "是否要打开文件地址"
    else:
        title = search_title(os.path.dirname(file_title)) + '\r' + "是否复制到剪切板"
    result = tkinter.messagebox.askquestion(title = '复制标题' ,message= title)#弹出提示框
    if get_title == None:
        if result == "yes":
            print(os.path.dirname(file_title))
            os.startfile(os.path.dirname(file_title))
    else:
        if result == "yes":
            print(get_title)
            pyperclip.copy(get_title)

wallpaper_path_list = search_file(wallpaper_path,file_type)


btn_Play_video = tkinter.Button(player,text = "随机视频",height=2,width=8,command = Play_video)#播放随机视频
btn_Play_video.place(x=45,y=20)
btn_title = tkinter.Button(player,text = "复制标题",height=2,width=8,command = list_title)#列出标题并复制到剪切板

btn_title.pack_forget()

player.mainloop()
