from domaincolorutil import DomainColorUtil
import os
import openpyxl
import matlab
import matlab.engine


def open_one_file(image_path):
    colorutil = DomainColorUtil(image_path)
    print(colorutil.get_domamin_color())


def walk_through():
    for root, dirs, files in os.walk("img", topdown=False):
        for name in files:
            open_one_file(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


def read07Excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb.get_sheet_by_name('sheet1')
    for row in sheet.rows:
        for cell in row:
            print(cell.value, "\t")
        print()

# def openExcel():
#     for root, dirs, files in os.walk("xlsx", topdown=False):
#         for name in files:
#             read07Excel(os.path.join(root, name))

def test():
    print()


if __name__ == '__main__':
    # openExcel()
    # walk_through()
    test()
