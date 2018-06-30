class Person():

    def __init__(self):
        self._name="hh"
        self._age=0
    def fget(self):
        return self._name,self._age
    def fset(self,value):
        self._name=value.upper()
    def fset1(self,value):
        self._age=int(value)
    def fdel(self):
        del self._name
        del self._age
    name=property(fget,fset,fdel)
    age=property(fget,fset1,fdel,"如下操作")
p1=Person()
print(p1.__dict__)
p1.name="Lhm"
p1.age=19.8
print(p1.__dict__)
print(p1.name)
print(p1.__dict__)

