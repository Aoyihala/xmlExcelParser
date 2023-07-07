import xmlParse
import constants
import os
import constants
import main
import utils


def clickPathDir():
    dirpath = main.showAndReturnPathSelector
    if utils.checkDirIsAndroidLan(dirpath):
        constants.xmlspathDir = dirpath
    else:
        main.callbackMessage("文件夹内容不符合")
    


def clickModel3(key,value):
    constants.xmlKey = key
    constants.xmlValue = value
    
    