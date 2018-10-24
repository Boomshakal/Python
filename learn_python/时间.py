import calendar  #获取日历

year = input("请输入年份：")
print ("你输入的内容是: " + year) 
month = input("请输入月份：") 
print ("你输入的内容是: " + month) 
cal = calendar.month(int(year), int(month))
s="以下是{0}年{1}月日历表：".format(year,month)
print (s)
print (cal)