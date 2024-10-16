import datetime
import xlwt
import os
from openpyxl import Workbook as wb
from openpyxl.reader.excel import load_workbook


folderLocation = "C:\\Users\\mirac\\OneDrive\\Desktop\\Inventory-Intro-to-Software-Dev-main\\Inventory-Intro-to-Software-Dev-main\\Inventory Files\\Excel Sheets\\Excel Sheet"

# Finds Current Date, Allows for File Management
current_time = datetime.datetime.now()
month = str(current_time.month) + '-'
day = str(current_time.day) + '-'
year = str(current_time.year)
date = month+day+year
# print(date)

# Defines file location for new file
excelName = "Inventory-"+ date + ".xlsx"
newFileLocation = folderLocation + '\\' + excelName
print(newFileLocation)

# Default File, It must have this on the file
for filename in os.listdir(folderLocation):
    if filename.endswith(".xlsx"):
        copyPath = os.path.join(folderLocation, filename)
        print(filename)
    else:
        wb = Workbook()
        ws = wb.active
        ws['A1'] = "Category"
        ws['B1'] = "Item"
        ws['C1'] = "InStock"
        ws['D1'] = "Purchased"
        ws['E1'] = "Price"
        ws['F1'] = "Availability"
        ws['G1'] = "Link"
        ws['H1'] = "Entry Date"


wb.save(filename)
