import pandas as pd
from Validation import *
import Main

def importFile(fname):
    workbook = pd.ExcelFile(fname)
    df = pd.read_excel(workbook,'Sheet1')

    employeeID = df.EmployeeID
    account_number = df.account_number
    joining_date = df.joining_date
    #print (str(employeeID))
    validate("EmployeeID", employeeID)

#importFile(r'C:\Users\parthnigam7\Desktop\Eval\TestData.xlsx')
