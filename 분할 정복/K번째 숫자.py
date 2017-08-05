# Enter n, m , lsit
n, m = map(int, input().split())
l=list(map(int, input().split())); mat=[]

# Define Constant
MAX = m

# Matrix Define
matrix=[[0 for i in range(MAX)] for i in range(MAX)]

for i in range(m):
    matrix[i]=list(map(int, input().split()));

for i in range(m):
    print(type(l))
    new_list = l[matrix[i][0]-1:matrix[i][1]]
    print(new_list.sort())
    # print(sorted_list)

print(new_list)


