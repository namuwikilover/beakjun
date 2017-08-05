import sys

N_list=[]; M_list=[]

# N input
N=int(sys.stdin.readline()[:-1])
N_list=list(map(int, sys.stdin.readline()[:-1].split()))

# M input
M=int(sys.stdin.readline()[:-1])
M_list=list(map(int, sys.stdin.readline()[:-1].split()))

# result output
for M_item in M_list:
    if M_item in N_list: print('1')
    else: print('0')
