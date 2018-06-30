class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
print(D.__mro__)
print(issubclass(D,B))  #检测D是不是B的类
print(issubclass(D,C))  #检测D是不是C的类