
from Logic import *
issueArray = []

lengthparam = 0


configList = {"EmployeeID": {"formatCheck": 10, "nullCheck": 0}, "accountNumber": {"formatCheck": 5, "nullCheck": 0}, "JoiningDate": {"formatCheckDate": "%d %b %y", "nullCheck": 0}}
#get from config file
result =[]
def validate(arrayName, List):
    #get lengthParam from flask file
    for items in configList:
        print (items)

    if arrayName not in configList:
        print ("returning")
        return True

    myList = configList.__getitem__(arrayName)

    """for items in myList:
        print (items)
    """
    #for loop for traversing config file

    for checks in myList:
        for index in range(len(List)):
            #print (type(List[index]))
            returnValue= globals()[checks](List[index],myList[checks])
            if returnValue!=1:
                result.append([index, returnValue])
    print(str(result))





"""
  if arrayName=="EmployeeID":
        for i in range(len(list)):
            if ~validateEmployeeId(list[i], lengthparam):
                issueArray[count].append(i)
                issueArray[count].append(list['employeeID']['lengthValidate'])
                count+=1
            if nullCheck(list[i]):
                issueArray[count].append(i)
                issueArray[count].append(list['employeeID']['nullCheck'])
                count+=1

"""












