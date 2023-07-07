import openpyxl
import langurageFactory
import tkinter as tk
from tkinter import filedialog
import tinkerUI
import utils
import constants
import threading
from threading import *


def main():
    window = tk.Tk()
    window.title("多语言转换器")
    window.geometry("600x300")
    tinkerUI.init(window)
    tinkerUI.addButtonAndDes(buttonClick)
    tinkerUI.addButtonAndDes2(clickOldXml=clickOldXml,clickNewXml=clickNewXml,clickCallBackmodel=clickMode2)
    window.mainloop()
 


def buttonClick():
    # 打开文件选择对话框
    file_path = showAndReturnFileSelector()
    if utils.checkPathIsExcel(file_path):
        print("选择的文件路径：", file_path)
        thread = threading.Thread(target=langurageFactory.parseXlsx(file_path,callbackMessage))
        thread.start()
      
    else:
        tinkerUI.showErrorLabel("文件格式错误")    

def clickOldXml():
    file_path = showAndReturnFileSelector()
    if utils.checkPathIsXml(file_path):
        print("选择的文件路径：", file_path)
        constants.pathOldXml = file_path
        tinkerUI.labelOldXml.configure(text=file_path)
    else:
        tinkerUI.showErrorLabel("文件格式错误")    

def clickNewXml():
    file_path = showAndReturnFileSelector()
    if utils.checkPathIsXml(file_path):
        print("选择的文件路径：", file_path)
        constants.pathNewXml = file_path
        tinkerUI.labelNewXml.configure(text=file_path)
    else:
        tinkerUI.showErrorLabel("文件格式错误")    
    
def clickMode2():
    thread = threading.Thread(target= langurageFactory.initModel2(constants.pathOldXml,constants.pathNewXml,callbackMessage))
    thread.start()
         



def showAndReturnFileSelector():
    # 创建一个隐藏的根窗口
    root = tk.Tk()
    root.withdraw()
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename()
    root.destroy()    
    return file_path


def callbackMessage(data:str):
    tinkerUI.showMesssageWindow(data)


if __name__ == "__main__":
    main()

    
    
