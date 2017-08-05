import heapq
import random
import sys

def heap_sort(items):
    heapq.heapify(items)
    items[:] = [heapq.heappop(items) for i in range(len(items))]

l = []
N = int(sys.stdin.readline()[:-1])
for i in range(N) :
    l.append(int(sys.stdin.readline()[:-1]))

heap_sort(l)
for i in l:
    print(i)
# print("\n".join(l))
