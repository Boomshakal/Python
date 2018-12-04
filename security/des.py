import crypt
import random
import string
chars=string.digits+string.ascii_letters
print(chars)

def getsalt(chars):
    return random.choice(chars)+random.choice(chars)

salt=getsalt(chars)
print(salt)

msg=crypt.crypt('hello,world!',salt)
print(msg)