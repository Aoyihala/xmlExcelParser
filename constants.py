# xlsx使用的变量
listConst:list = []
listFilter:list = []
listLanguage:list = []

# xml使用的变量
pathOldXml:str
pathNewXml:str
listOldXmlNames = []
listNewXmlNames = []
mapOldXml = {}
mapNewXml = {}


#语言实体bean
class LanguageBean:
    def __init__(self):
        self.languageXmlCode = ""
        self.nameMap = {}
#通过title获取语言文件夹名称
def getLanguageFilterByTitle(string):
    if string == "中文":
        return "values-zh-rCN"
    elif string == "俄语":
        return "values-ru"
    elif string == "阿语":
        return "values-ar"
    elif string == "西班牙语":
        return "values-es"
    elif string == "葡萄牙语":
        return "values-pt"
    elif string == "乌克兰语":
        return "values-uk"
    elif string == "土耳其语":
        return "values-tr"
    elif string == "波斯语":
        return "values-fa"
    elif string == "希伯来语":
        return "values-iw"
    elif string == "意大利语":
        return "values-it"
    elif string == "泰语":
        return "values-th"
    else:
        return ""
