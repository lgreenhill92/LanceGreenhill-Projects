from itertools import zip_longest
import pandas as pd
import numpy as np
import openpyxl
import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell

# rb1 = xlrd.open_workbook('C:/Local files/Testfolder/AutotestHourlyExportNoedit.xlsx')
# rb2 = xlrd.open_workbook('C:/Local files/Testfolder/AutotestHourlyExportedited.xlsx')

#def return_home(template_file_location, template_file_name, test_file_location, test_file_name ):

template = pd.read_excel("C:/Local files/Testfolder/AutotestHourlyExportNoedit.xlsx", na_values=np.nan, header=None)
testSheet = pd.read_excel("C:/Local files/Testfolder/AutotestHourlyExportedited.xlsx", na_values=np.nan, header=None)

print(template)
print(testSheet)
rt, ct = template.shape
rtest, ctest = testSheet.shape

df = pd.DataFrame(columns=['Cell_Location', 'BaseTemplate_Value', 'CurrentFile_Value'])
i = 0
rowcount = range(max(rt, rtest))
for rowNo in range(max(rt, rtest)):
    i += 1
    for colNo in range(max(ct, ctest)):
        # Fetching the template value at a cell
        try:
            template_val = template.iloc[rowNo, colNo]
        except:
            template_val = np.nan

        # Fetching the testsheet value at a cell
        try:
            testSheet_val = testSheet.iloc[rowNo, colNo]
        except:
            testSheet_val = np.nan

        # Comparing the values
        if str(template_val) != str(testSheet_val):
            cell = xl_rowcol_to_cell(rowNo, colNo)
            dfTemp = pd.DataFrame([[cell, template_val, testSheet_val]],
                                  columns=['Cell_Location', 'BaseTemplate_Value', 'CurrentFile_Value'])
            df = pd.concat([df,dfTemp], ignore_index=True)
    if df.empty:
        match = True
    elif i == (max(rowcount)):
        print("We may have a data change. Please verify locations")
        dfOut = df.to_string(index=False)
        print(f"{dfOut}\n")
        #print("Hello" + match + "")
        #match = True
    else:
        #print(i)
        #print(max(rowcount))
        #print("Data Error")
        dfOut = df.to_string(index=False)
        #print(f"{dfOut}\n")
        match = False
    #print("\n")


"""
I need to merge this data with the test case to review exports now.
"""