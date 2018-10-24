
from urllib import request, parse
from http import cookiejar

#  创建cookiejar的实例
cookie = cookiejar.CookieJar()

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)

def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''

    # 此url需要从登录form的action属性中提取
    url = "http://eip.megmeet.com:8008/login.jsp"

    # 此键值需要从登录form的两个对应input中提取name属性
    data = {
        "j_username": "yhs375",
        "j_password": "lhm9223572309"
    }

    # 把数据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=bytes(data,encoding='utf-8'))

    # 使用opener发起请求
    response = opener.open(req)
    #print(response)

def getHomePage():
    url = "http://eip.megmeet.com:8008/sys/portal/page.jsp"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)


    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()