from openpyxl import load_workbook

# 使用load_book方法读取excel
wb = load_workbook(filename='empty_book.xlsx')
# 指定表名称
sheet_ranges = wb['range names']
# 输出sheet表D18的值
print(sheet_ranges['D18'].value)