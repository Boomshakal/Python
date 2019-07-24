import os
import threading
import socket
from tkinter import *
from tkinter.filedialog import askdirectory
from ip import public_ip


def share(path, port):
    # 可指定路径
    os.chdir(path)
    os.system('python -m http.server {}'.format(port))


def selectPath():
    path_ = askdirectory()
    path.set(path_)


def execute_share():
    th = threading.Thread(target=share, args=(path.get(), port.get()))
    th.setDaemon(True)
    th.start()


root = Tk()
path = StringVar()
port = StringVar()
ip = public_ip()

Label(root, text="目标路径:").grid(row=0, column=0)
Entry(root, textvariable=path).grid(row=0, column=1)
Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
Label(root, text=ip).grid(row=1, column=0)
# Label(root, text="浏览器输入：'IP:8080'").grid(row=1, column=1)
Entry(root, textvariable=port).grid(row=1, column=1)
Button(root, text="共享", command=execute_share).grid(row=1, column=2)

root.mainloop()
