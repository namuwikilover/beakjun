import queue as Queue
queue = Queue.Queue()    

M, N = map(int, input().split()); Matrix=[]
for i in range(N):
    Matrix.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if Matrix[i][j]==1: 
            ix=i; iy=j
    
queue.put([ix, iy]); count=0 # BFS 시작

while queue:
    curr = queue.get(); count+=1
    print(curr);
    if [0, 0] == curr:
        print(int(count/3))
        break
    if curr[0]<4 and curr[0]>=0 and curr[1]+1<6 and curr[1]+1>=0:
        if Matrix[curr[0]][curr[1]+1]==0: 
            Matrix[curr[0]][curr[1]+1]=1    
            queue.put([curr[0], curr[1]+1])
        
    if curr[0]+1<4 and curr[0]+1>=0 and curr[1]<6 and curr[1]>=0: 
        if Matrix[curr[0]+1][curr[1]]==0:
            Matrix[curr[0]+1][curr[1]]=1    
            queue.put([curr[0]+1, curr[1]])
        
    if curr[0]<4 and curr[0]>=0 and curr[1]-1<6 and curr[1]-1>=0: 
        if Matrix[curr[0]][curr[1]-1]==0:
            Matrix[curr[0]][curr[1]-1]=1    
            queue.put([curr[0], curr[1]-1])
        
    if curr[0]-1<4 and curr[0]-1>=0 and curr[1]<6 and curr[1]>=0: 
        if Matrix[curr[0]-1][curr[1]]==0:
            Matrix[curr[0]-1][curr[1]]=1
            queue.put([curr[0]-1, curr[1]])
    
    



