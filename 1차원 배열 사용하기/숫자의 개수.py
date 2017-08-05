d={k:0 for k in range(10)}
s=1
for i in range(3):
    a=int(input())
    s*=a
for i in str(s):
    if int(i) in d:
        d[int(i)]+=1
for i in range(10):
    print(d[i])