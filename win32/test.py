from pywinauto.application import Application
import time

# Run a target application
app = Application().start("notepad.exe")
time.sleep(1)
# Select a menu item
app[u'无标题-记事本'].menu_select(u"帮助->关于记事本")
time.sleep(2)
app[u'关于"记事本"'][u'确定'].click()
time.sleep(1)
# inter something
app[u'无标题-记事本'].Edit.type_keys(u"测试!", with_spaces=True)
time.sleep(1)
app[u'无标题-记事本'].menu_select(u'文件->另存为...')
time.sleep(1)
app[u'另存为']['edit'].type_keys(str(time.time()) + ".txt")
time.sleep(1)
app[u'另存为'][u'保存'].click()
time.sleep(1)
app.Notepad.menu_select(u'文件->退出')
