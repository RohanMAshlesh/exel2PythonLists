from xlrd import open_workbook

book = xlrd.open_workbook("##File_path") #use the  of excel file in actual code.
sheet = book.sheet_by_index(0)

list_r = []

for i in range(1,sheet.nrows):
    list_r.append(str(sheet.row_values(i)[r-1]))
        
