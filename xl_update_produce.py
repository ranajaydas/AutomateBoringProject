""" Program to update the prices in an excel file, xl_produceSales.xlsx """

import openpyxl

print('Opening workbook...')
wb = openpyxl.load_workbook('xl_produceSales.xlsx')
sheet = wb['Sheet']

# All the prices that need to be updated in xl_produceSales.xlsx
price_updates = {'Garlic': 3.77,
                 'Celery': 1.77,
                 'Lemon': 1.42}

for row in range(2, sheet.max_row+1):
    produce_name = sheet.cell(row=row, column=1).value
    if produce_name in price_updates:
        sheet.cell(row=row, column=2).value = price_updates[produce_name]

print('Saving new workbook with updated prices...')
wb.save('xl_produceSales_updated.xlsx')
