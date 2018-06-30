try:
    num =int(input("请输入被除数："))
    rst =100/num
    #raise DanaZeroDivisionError
    print("计算结果为：{0}".format(rst))
except ZeroDivisionError as e:
    print("你输入的有问题")
    print(e)
    print(e.__str__())
    print(ZeroDivisionError.__dict__)
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
except Exception as e:
    print(e)
#except DanaZeroDivisionError as e:
#    print(DanaZeroDivisionError )
else:
    print("程序没有问题")
finally:
    print("反正我会被执行")

#raise 异常，则推荐自定义异常
#class DanaZeroDivisionError(ZeroDivisionError):
#      pass
