import xmlParse
import constants
import os
import constants
import main
import utils
import iso639
import pycountry

floderSubNmae:list
def clickPathDir():
    dirpath = main.showAndReturnPathSelector()
    if utils.checkDirIsAndroidLan(dirpath):
        constants.xmlspathDir = dirpath
        print("语言",pycountry.languages)
        getChildFloder(dirpath)
    else:
        main.callbackMessage("文件夹内容不符合")
    
    
    
def getChildFloder(folder_path):
    # 获取指定文件夹中的所有一级文件夹
    subfolders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

    # 打印一级文件夹名称
    for subfolder in subfolders:
        print(subfolder)



def clickModel3(key,value):
    constants.xmlKey = key
    constants.xmlValue = value
    
    