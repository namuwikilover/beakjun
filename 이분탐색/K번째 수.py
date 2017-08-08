# N=int(input()); K=int(input())
# l1=[[i*j for i in range(1, N+1)] for j in range(1, N+1)]
# l2=[value for sublist in l1 for value in sublist]
# l2.sort()
# print(l2[K-1])
N=int(input()); K=int(input())
l1=[[i*j for i in range(1, N+1)] for j in range(1, N+1)]
l1=[value for sublist in l1 for value in sublist]
l1.sort()
print(l1[K-1])