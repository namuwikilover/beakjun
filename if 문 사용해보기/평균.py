N=int(input())
l=list(map(int, input().split())); M=max(l)
for i in range(len(l)):
    l[i]=l[i]/M*100
print("%.2f" % float(sum(l)/len(l)))
