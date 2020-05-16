class A(object):
    def __init__(self, name):
        self.name = name


class B(object):
    __slots__ = ('name',)

    def __init__(self, name):
        self.name = name

a = A('li')
a.age = 28
print(a.name)
print(a.__dict__)

b = B('min')

# 'B' object has no attribute
# b.age = 29
# print(b.__dict__)