class A():
    def __init__(self):
        print("这是A")
class B(A):
    def __init__(self,name):
        print("这是B")
        print(name)
class C(B):
    def __init__(self,name):
        #B.__init__(self,name)
        super().__init__(name)
        #super(C,self).__init__(name)
        print("这是C附加功能")

c = C("这是c")
#print(type(super))
#print(help(super))