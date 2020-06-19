def result_mohu(key, str):
    i = 0
    j = 0
    k = 0
    flag = 0
    len_key = len(key)
    # print(len_key)
    len_str = len(str)
    # print(len_str)
    while i < len_str and j < len_key:
        # 遇到一个相同的字符就继续往后匹配
        # print(key[j])
        if key[j] == str[i]:
            k += 1
            j += 1
            i += 1
            # print(key[j])
            if k == len_key:
                flag = 1
                break
        # 又回退到最初的起点
        else:
            j -= k
            i = i - k + 1
            k = 0
    return flag

# KMP算法
class KMP(object):
    def __init__(self, ss: str) -> list:
        self.length = len(ss)
        self.next_lst = [0 for _ in range(self.length)]
        self.next_lst[0] = -1
        i = 0
        j = -1
        while i < self.length - 1:
            if j == -1 or ss[i] == ss[j]:
                i += 1
                j += 1
                self.next_lst[i] = j
            else:
                j = self.next_lst[j]
        self.pattern = ss

    def match_str(self, ss: str):
        ans_lst = []
        j = 0
        for i in range(len(ss)):
            if ss[i] != self.pattern[j]:
                j = self.next_lst[j] if self.next_lst[j] != -1 else 0
            if ss[i] == self.pattern[j]:
                j += 1
            if j == self.length:
                return i + 1 - self.length
        return -1


if __name__ == '__main__':
    # print(a[0])
    # a = ['2341111', '23445111', '231231']
    # for j in a:
    #     res = result_mohu('234', j)
    #     if res == 1:
    #         print(j)

    tmp_kmp = KMP('iabc')
    print(tmp_kmp.match_str('adosjfoiajsoifjasiofjoiasdjoiabc'))

    if result_mohu('iabc','adosjfoiajsoifjasiofjoiasdjoiabc'):
        print('inside')
