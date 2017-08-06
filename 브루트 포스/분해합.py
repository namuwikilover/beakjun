N=int(input());
f=0; check=0; result=0
for i in range(100000):
    for j in str(i):
        result+=int(j)
    if result+int(i)==N:
        print(j)
        break
    result=0