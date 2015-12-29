import xlwt

book = xlwt.Workbook(encoding="utf-8")

#With a workbook object made we can now add some sheets.

sheet1 = book.add_sheet("Python Sheet 1") 
sheet2 = book.add_sheet("Python Sheet 2") 
sheet3 = book.add_sheet("Python Sheet 3")

#We have now formed a workbook object which we can add data to before outputting it to the file system. Adding information to a spreadsheet is simply a case of using the write() function of the sheet objects we created before.

sheet1.write(0, 0, "This is the First Cell of the First Sheet") 
sheet2.write(0, 0, "This is the First Cell of the Second Sheet") 
sheet3.write(0, 0, "This is the First Cell of the Third Sheet") 
sheet2.write(1, 10, "This is written to the Second Sheet") 
sheet3.write(0, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(1, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(2, 2, "This is part of a list of information in the Third Sheet") 
sheet3.write(3, 2, "This is part of a list of information in the Third Sheet")

#After the spreadsheet is formed, the sheets are added and the data is written it is time to commit our new spreadsheet to the file system. To do this we use the book's save() method, passing the path to the file as a parameter. If a file already exists where you intend to save your spreadsheet it will be overwritten.

book.save("python_spreadsheet.xls")