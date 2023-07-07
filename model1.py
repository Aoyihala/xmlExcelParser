import openpyxl
from openpyxl import *
import constants
import os
import shutil
import zipfile
import subprocess



folder = "excelfile/"    
def genrateXmlFile(callback):
    for language in constants.listLanguage:
        language:constants.LanguageBean
        path_dir = os.path.join(folder, "values", language.languageXmlCode)
        os.makedirs(path_dir, exist_ok=True)
        
        map_new = {}
        if len(constants.listFilter) > 0:
            for filter_value in constants.listFilter:
                if filter_value in language.nameMap:
                    map_new[filter_value] = language.nameMap[filter_value]
        else:
            map_new = language.nameMap
        generateStringsXml(map_new, os.path.join(os.path.abspath(path_dir), "strings.xml"),callback)
    source_folder_path = os.path.join(folder, "values")
    destination_zip_file_path = os.path.join(folder, "language.zip")
    callback("压缩中\n.............................................")
    zipFolder(source_folder_path, destination_zip_file_path)
    callback("压缩完成，路径为" + destination_zip_file_path)


def zipFolder(sourceFolderPath, destinationZipFilePath):
    with zipfile.ZipFile(destinationZipFilePath, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(sourceFolderPath):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, sourceFolderPath))
    path_dir = os.path.join(folder, "values")
    shutil.rmtree(path_dir)
    subprocess.run(["explorer", os.path.abspath(destinationZipFilePath)])
    
def generateStringsXml(data_map, file_path,callback):
    with os.fdopen(os.open(file_path, os.O_RDWR | os.O_CREAT), "w", encoding="utf-8") as file_obj:
        file_obj.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
        file_obj.write("<resources>\n")
        for key, value in data_map.items():
            file_obj.write(f"\t<string name=\"{key}\">{value}</string>\n")
        file_obj.write("</resources>\n")
    callback("生成xml" + file_path + "\n")