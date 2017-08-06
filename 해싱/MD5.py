import hashlib
import binascii
m = hashlib.md5()

l=input().encode('utf-8')
m.update(l)
print(m.hexdigest())