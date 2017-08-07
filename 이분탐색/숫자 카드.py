import sys

def binSearch(ary, elem, first, last):
    if (first > last):
        return False
    mid = int((first + last) / 2)
    if (ary[mid] < elem):
        return binSearch(ary, elem, mid + 1, last)
    elif (ary[mid] > elem):
        return binSearch(ary, elem, first, mid - 1)
    else:
        return True

N_list=[]; M_list=[]; result=[]
N=int(sys.stdin.readline()[:-1]); N_list=list(map(int, sys.stdin.readline()[:-1].split()))
M=int(sys.stdin.readline()[:-1]); M_list=list(map(int, sys.stdin.readline()[:-1].split()))

N_list.sort()
for M_item in M_list:
    if binSearch(N_list, M_item, 0, len(N_list)-1) == True: print('1', end=' ')
    else: print('0', end=' ')

