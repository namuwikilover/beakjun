import sys

def countingsort( aList, k ):
    counter = [0] * ( k + 1 )
    for i in aList:
      counter[i] += 1
 
    ndx = 0;
    for i in range( len( counter ) ):
      while 0 < counter[i]:
        aList[ndx] = i
        ndx += 1
        counter[i] -= 1

l = []
N = int(sys.stdin.readline()[:-1])
for i in range(N) :
    l.append(int(sys.stdin.readline()[:-1]))

countingsort(l, max(l))
for i in l:
    print(i)