#import numpy as np
from pylab import*

mpl.rcParams['font.sans-serif'] = ['SimHei']
# 上面两行代码解决matplotlib绘图不能显示中文问题
# 解决负号'-'显示为方块的问题
matplotlib.rcParams['axes.unicode_minus'] = False

import matplotlib.pyplot as plt

n_groups = 10

# 城市分布数量权值

city_weight = (36.14,3.47,2.97,2.97,2.72,1.49,1.49,1.24,0.74,0.74)

fig, ax = plt.subplots()

index = np.arange(n_groups)

bar_width = 0.35

opacity = 0.4

error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, city_weight, bar_width,alpha=opacity, color='b', error_kw=error_config,label='城市')

ax.set_xlabel('城市名称')

ax.set_ylabel('数据占比(%)')

ax.set_title('好友城市Top10')

ax.set_xticks(index + bar_width / 2)

ax.set_xticklabels(('台州', '温州', '深圳', '杭州', '株洲','黄冈', '宁波', '武汉', '金华', '宜宾'))

ax.legend()

fig.tight_layout()

plt.show()