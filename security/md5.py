import hashlib
m=hashlib.md5()
m.update(b'hello,word!')
b=m.hexdigest()
print(b)