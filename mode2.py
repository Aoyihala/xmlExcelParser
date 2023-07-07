import xmlParse
import constants

def compareXml(oldPath,newPath,callBack):
   constants.listOldXmlNames,constants.mapOldXml = xmlParse.parseXml(oldPath,callBack)
   constants.listNewXmlNames,constants.mapNewXml = xmlParse.parseXml(newPath,callBack)
   #合并listOldXmlNames和listNewXmlNames，合并字典constants.mapOldXml和字典constants.mapNewXml
   merged_xml_names = list(set(constants.listOldXmlNames + constants.listNewXmlNames))
   merged_xml_map = {**constants.mapOldXml, **constants.mapNewXml}
   callBack("开始合并到新xml\n")
   xmlParse.createNewXml(merged_xml_names,merged_xml_map,callBack)