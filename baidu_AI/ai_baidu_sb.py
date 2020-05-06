from aip import AipSpeech

# https://ai.baidu.com/ai-doc/SPEECH/Gk4nlz8tc
""" 你的 APPID AK SK """
APP_ID = '19732493'
API_KEY = '8U3CErblpdDr1HDaGKTroVf1'
SECRET_KEY = 'RxsyoCKvMEle6HoXpjw0gIUSSGiUR7UC'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# print(client)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = client.asr(get_file_content('audio.pcm'), 'pcm', 16000, {
    'dev_pid': 1537,
})

print(result.get('result')[0])