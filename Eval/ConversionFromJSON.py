import json
import demjson
from OpenExcel import *
list = []
def getData(jsonString):
    #print (address)
    #address.split(str("\"))
    #address = address.replace("\", "//")
    #print (address)
    temp = demjson.decode(jsonString)
    address = temp['path']
    print(address)
    importFile(address)

jsonString =demjson.encode({"path": "C:/Users/parthnigam7/Desktop/Eval/testData.xlsx"})

getData(jsonString)