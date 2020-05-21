##  Map函数返回一个列表，该列表由对序列中的每个元素应用一个函数时返回的值组成。
# def add_three(x):
#     return x + 3
# li = [1,2,3]
# print(list(i for i in map(add_three, li)))
# => [4, 5, 6]

# # reduce接受一个函数和一个序列，然后对序列进行迭代。在每次迭代中，当前元素和前一个元素的输出都传递给函数。最后，返回一个值
# from functools import reduce
# def add_three(x,y):
#     return x + y
# li = [1,2,3,5]
# print(reduce(add_three, li))
# => 11

# def add_three(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# li = [1,2,3,4,5,6,7,8]
# print(list(i for i in filter(add_three, li)))
# => [2, 4, 6, 8]


# Python中函数参数是引用传递（注意不是值传递）。对于不可变类型（数值型、字符串、元组），因变量不能修改，所以运算不会影响到变量自身
# 而对于可变类型（列表字典）来说，函数体运算可能会更改传入的参数变量。
a = [1, 2]
b = {'a': 1, 'b': 2}
c = {'c': 3, 'd': 4}


def add_three(a, *args, **kwargs):
    a.append(3)
    print(a)
    print(args)
    print(kwargs)


add_three(a, b, kw=c)
print(a)
