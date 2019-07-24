def result_mohu(key, str):
    i = 0
    j = 0
    k = 0
    flag = 0
    len_key = len(key)
    #print(len_key)
    len_str = len(str)
    #print(len_str)
    while i < len_str and j < len_key:
        #遇到一个相同的字符就继续往后匹配
        #print(key[j])
        if key[j] == str[i]:
            k +=1
            j +=1
            i +=1
            #print(key[j])
            if k == len_key:
                flag = 1
                break
        # 又回退到最初的起点
        else:
            j -= k
            i = i - k + 1
            k = 0
    return flag

if __name__ == '__main__':
    #print(a[0])
    a=['2341111','23445111','231231']
    for j in a:
        str=result_mohu('234',j)
        if str==1:
            print(j)