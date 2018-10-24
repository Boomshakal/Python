from wxpy import *
bot=Bot(cache_path=True)

#bot.file_helper.send("hello,I'm lhm")
''' 给个人发送消息
my_friend=bot.friends().search('小号')[0]
my_friend.send('Hello WeChat!')
'''
'''
t0 = bot.friends(update=False)
print("我的好友数："+str(len(t0)-1))
t1=bot.groups(update=False)
print("我的群数："+str(len(t1)))
t2=bot.mps(update=False)
print("我的微信公众号数："+str(len(t2)))
'''
#'''图灵机器人
tuling=Tuling(api_key='c1c0be3bfa7f461c926ea40a25cbeb71')
print('微信机器人已经启动')
# 如果想对所有好友实现机器人回复把参数my_friend改成chats = [Friend]
my_friend=bot.friends().search('惠达闫海波')[0]

@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

# 进入交互式的 Python 命令行界面，并堵塞当前线程

embed()
#'''
#my_friends = bot.friends(update=False)
#print(my_friends.stats_text())


