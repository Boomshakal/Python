import re
# str = """ lr<lr@ikahe.net>
# xuguochun<xuguochun@ikahe.net>,   lxw<lxw@ikahe.net>,   zhangcheng<zhangcheng@ikahe.net>,   yft<yft@ikahe.net>,   sdj<sdj@ikahe.net>,   xudewei<xudewei@ikahe.net>,   maxinhong<maxinhong@ikahe.net>,   姜连洋<jianglianyang@ikahe.net>,   cg<cg@ikahe.net>,   gongsaikang<gongsaikang@ikahe.net>,   马臻<mazhen@ikahe.net>,   hhmeg<hhmeg@megmeet.com>,  刘勇<liuyong@ikahe.net>,   邱勇<qiuyong@ikahe.net>,   wanglin<wanglin@ikahe.net>,   zhumaoqun<zhumaoqun@ikahe.net>,   quxuehui<quxuehui@ikahe.net>,   wxy<wxy@ikahe.net>,   zhouxiaobo<zhouxiaobo@ikahe.net>,   huangcao<huangcao@ikahe.net>,   wj<wj@ikahe.net>,   wangchuanyong<wangchuanyong@ikahe.net>,      黄强<huangqiang@ikahe.net>,   yinqinai@ikahe.net<yinqinai@ikahe.net>， cwj<cwj@ikahe.net,xgq<xgq@ikahe.net>，解根雄<jiegenxiong@ikahe.net>,jiangshaoting<jiangshaoting@ikahe.net>
# yjg<yjg@ikahe.net>，zhangcheng<zhangcheng@ikahe.net>
# """
#
# it = re.finditer(r"[a-zA-Z0-9_-]+@[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)",str)
# for match in it:
#     print (match.group(0))


str= '{"errcode":0,"access_token":"134a803d3b3831168acfeeb001ff0f3f","errmsg":"ok","expires_in":7200}'
import re

pattern = re.compile(r'"access_token":"(.*?)"')  # 查找数字
result1 = pattern.findall(str)

print(result1)