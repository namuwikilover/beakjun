import hashlib
m = hashlib.sha224()
l=input().encode('utf-8')
m.update(l)
print(m.hexdigest())