def func(*args):
    size = len(args)
    idx = 1
    i = args[0]
    f = 0
    while idx < size:
        j = args[idx]
        # 用辗转相除法求i,j的最大公约数m
        b = i if i < j else j  # i，j中较小那个值
        a = i if i > j else j  # i,j中较大那个值
        r = b  # a除以b的余数
        while r != 0:
            r = a % b
            if r != 0:
                a = b
                b = r
        f = i * j / b  # 两个数的最小公倍数
        i = f
        idx += 1
    return f


print(func(4, 3, 5))

dit = {
    '1':'qwe',
    '2':'asd'
}
print(dit.get('3',''))