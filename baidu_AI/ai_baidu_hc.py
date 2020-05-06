from aip import AipSpeech

# https://ai.baidu.com/ai-doc/SPEECH/Gk4nlz8tc
""" 你的 APPID AK SK """
APP_ID = '19732493'
API_KEY = '8U3CErblpdDr1HDaGKTroVf1'
SECRET_KEY = 'RxsyoCKvMEle6HoXpjw0gIUSSGiUR7UC'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# print(client)

result = client.synthesis('来了，老弟', 'zh', 1, {
    'vol': 5,
    'per': 4,
    'spd': 3,
    'pit': 7
})

# print(result)

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
