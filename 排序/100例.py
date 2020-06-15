# a = [1, 4, 2, 3, 1]
# b = set(a)
# if len(a) > len(b):
#     print('有重复值')
# print(type(b), b)
#
# # 计算字符串型表达式的值
# s = "1 + 3 + 5"
# res = eval(s)
# print(res)
#
#
#
# str = 'python'
# str1 = '_'.join(str)
# print(str1)
#
# import calendar
# from datetime import date
# mydate=date.today()
# print(calendar.calendar(2020))
#
# print(9/5,9//5,9%5,divmod(9,5))
#
# # import calendar
# # from datetime import date
# # mydate = date.today()
# # is_leap = calendar.isleap(mydate.year)
# # print(("{}是闰年" if is_leap else "{}不是闰年\n").format(mydate.year))

# x = map(str, (1, 3, 5))
# for e in x:
#     print(e, type(e))

x = [1, 2, 3, 5]
odd = filter(lambda e: e % 2, x)

for e in odd:  # 找到奇数
    print(e)
