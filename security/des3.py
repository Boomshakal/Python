# coding=utf-8

from Crypto.Cipher import DES3
from Crypto import Random
import binascii

key = '1234567890!@#$%^'
iv = Random.new().read(8)  #iv值必须是8位
cipher1 = DES3.new(key,DES3.MODE_OFB,iv)  #密文生成器，采用MODE_OFB加密模式
encrypt_msg =  iv + cipher1.encrypt('我是明文必须是八')
#附加上iv值是为了在解密时找到在加密时用到的随机iv,加密的密文必须是八字节的整数倍，最后部分
#不足八字节的，需要补位
print ('加密后的值为：',binascii.b2a_hex(encrypt_msg) )  #将二进制密文转换为16进制显示


cipher2 = DES3.new(key,DES3.MODE_OFB,iv) #解密时必须重新创建新的密文生成器
decrypt_msg = cipher2.decrypt(encrypt_msg[8:]) #后八位是真正的密文
print ('解密后的值为：',decrypt_msg)