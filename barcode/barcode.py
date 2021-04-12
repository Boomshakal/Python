import xlwt

from tkinter import *
from tkinter.filedialog import askdirectory


def base36_encode(number):
    num_str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if number == 0:
        return '0'

    base36 = []
    while number != 0:
        number, i = divmod(number, 36)  # 返回 number// 36 , number%36
        base36.append(num_str[i])

    return ''.join(reversed(base36))


def select_path():
    path_ = askdirectory()
    path.set(path_)
def execute():
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')

    begin = int(start.get(), 36)
    end = begin + int(num.get())
    for i in range(begin, end):
        worksheet.write(i - begin, 0, label=tm_qz.get() + ('00000' + base36_encode(i))[-5:])

    workbook.save(path.get() + '/barcode.xls')


root = Tk()

tm_qz = StringVar()
start = StringVar()
path = StringVar()
num = StringVar()

Label(root, text="条码前缀:").grid(row=0, column=0)
Entry(root, textvariable=tm_qz).grid(row=0, column=1)

Label(root, text="起始位置:").grid(row=0, column=2)
Entry(root, textvariable=start).grid(row=0, column=3)

Label(root, text="数量:").grid(row=0, column=4)
Entry(root, textvariable=num).grid(row=0, column=5)
Label(root, text="目标路径:").grid(row=1, column=0)
Entry(root, textvariable=path).grid(row=1, column=1)
Button(root, text="保存地址", command=select_path).grid(row=1, column=2)
Button(root, text="生成execl", command=execute).grid(row=1, column=3)

root.mainloop()
