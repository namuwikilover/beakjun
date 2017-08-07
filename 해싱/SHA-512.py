import hashlib
m = hashlib.sha512()
l=input().encode('utf-8')
m.update(l)
print(m.hexdigest())