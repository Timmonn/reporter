import openpyxl
book = openpyxl.open('ejecting_data.xlsx', read_only=True)
sheet = book.active
quantity_sell = {}
summa_sell = {}
profit = {}
for row in range(1,sheet.max_row+1):
 #  quantity_sell[sheet[row][0].value] = sheet[row][1].value
 #  summa_sell[sheet[row][0].value] = sheet[row][2].value
    profit[sheet[row][0].value] = sheet[row][3].value
print(profit)