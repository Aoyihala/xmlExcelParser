import tkinter as tk
from tkinter import font
from tkinter import *
window:Tk
labelError1:Label
labelOldXml:Label
labelNewXml:Label
#展示消息用
windowMessage:tk = None
labelMessage:Label


def showMesssageWindow(message):
    global windowMessage
    global labelMessage
    if windowMessage is not None and windowMessage.winfo_exists():
        # 窗口已经显示
        beforstr = labelMessage.cget("text")
        labelMessage.configure(text=beforstr+message)
        pass
    else:
        # 窗口未显示，可以创建并显示窗口
        windowMessage = tk.Toplevel()
        windowMessage.geometry("400x300")
        labelMessage = tk.Label(windowMessage, text=message)
        labelMessage.pack()

def init(rootWindow:Tk):
    global window
    window = rootWindow

def addButtonAndDes(clickCallBack):
     #创建一个窗口内部的label标签
    tk.Button(window,text="模式一",command=clickCallBack,
              bg="#FF0000", 
              fg="#FFFFFF",
              width=10,
              height=1).pack()
    tk.Label(window,text="点击后打开文件选择器，选择excel/xlsx文件，将里面的内容全部输出为安卓对应的语言文件string.xml").pack()
    
 
def addButtonAndDes2(clickOldXml,clickNewXml,clickCallBackmodel):
     #创建一个窗口内部的label标签
    global labelOldXml
    global labelNewXml 
    tk.Button(window,text="旧xml",command=clickOldXml,
              bg="#FF0000", 
              fg="#FFFFFF",
              width=10,
              height=1).pack()
    labelOldXml = tk.Label(window,text="")
    labelOldXml.pack()
    tk.Button(window,text="新xml",command=clickNewXml,
              bg="#FF0000", 
              fg="#FFFFFF",
              width=10,
              height=1).pack()
    labelNewXml = tk.Label(window,text="")
    labelNewXml.pack()
    tk.Button(window,text="模式2",command=clickCallBackmodel,
              bg="#FF0000", 
              fg="#FFFFFF",
              width=10,
              height=1).pack()
    tk.Label(window,text="点击上方xml按钮打开文件选择器，选择想xml文件，将里面的内容合并比对后输出一个新的语言文件string.xml").pack()
 
def showErrorLabel(message):
    global labelError1
    labelError1 = tk.Label(window,text=message,font=font.Font(size=16),fg="red")
    labelError1.pack(side=tk.BOTTOM,pady=10)


def hidenErrorLabel():
    if labelError1 is NONE:
        print("not init errorlabel")
    else:
        labelError1.pack_forget()    
    