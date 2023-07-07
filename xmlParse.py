import xml.etree.ElementTree as ET
import os
import xml.dom.minidom as minidom
import subprocess
# 解析指定路径的xml
def parseXml(path,callback):
    tree = ET.parse(path)
    # 遍历<string>元素并将name属性添加到列表
    name_list = []
    mapN = {}
    for string_element in tree.iter('string'):
        name_attribute = string_element.attrib['name']
        name_list.append(name_attribute)
        mapN[name_attribute] = string_element.text
    callback("解析xml路径:"+path+"\n")
    return name_list,mapN

# 创建xml文件
def createNewXml(name_list, mapN, callback):
    output_path = "xmlgenreate/"
    realPath = os.path.join(output_path)
    os.makedirs(realPath, exist_ok=True)  # 创建目录，如果目录已存在则忽略
    root = ET.Element("resource")
    for name in name_list:
        string_element = ET.SubElement(root, "string", name=name)
        string_element.text = mapN[name]

    tree = ET.ElementTree(root)
        # 修改文件权限为可写
    file_path = os.path.join(realPath, "strings.xml")
    open(file_path,"w")
    os.chmod(file_path, 0o777)  # 设置文件权限为可读、可写、可执行
    tree.write(file_path, encoding="utf-8", xml_declaration=True)
     # 使用minidom进行格式化
    dom = minidom.parse(file_path)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(dom.toprettyxml(indent="  "))
    callback("创建完成，路径"+os.path.abspath(file_path))
    subprocess.run(["explorer", os.path.abspath(file_path)])