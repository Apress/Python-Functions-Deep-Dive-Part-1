"""
An example of writing a large program
using a start-with-what-you-know approach
"""
import pathlib
import openpyxl


def get_worksheet():
    root_folder = pathlib.Path('')
    spreadsheet = root_folder / 'Documents' / 'names etc.xlsx'

    workbook = openpyxl.load_workbook(spreadsheet)
    sheet = workbook.active
    return sheet


# Throw away code, just so I can see what the rows look like
worksheet = get_worksheet()
for row in worksheet:
    print(row)
