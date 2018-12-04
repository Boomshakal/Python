from Crypto.Cipher import AES
from Crypto import Random
import binascii
key='1234567890!@#$%^'
iv= Random.new().read(16)

cipher1=AES.new(key,AES.MODE_CFB,iv)
encrypt_msg=iv+cipher1.encrypt('我是明文')
print('加密后的值为：',binascii.b2a_hex(encrypt_msg))

cipher2=AES.new(key,AES.MODE_CFB,iv)
decrypt_msg=cipher2.decrypt(encrypt_msg[16:])
print('解密后的值为：',decrypt_msg.decode('utf-8'))