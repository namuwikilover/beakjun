import queue as Queue
def bfs(graph,root,whatToFind):
    queue = Queue.Queue()
    queue.put(root)#put the first element in the queue, so we can explore it latter on
    while queue:#while there are elements in the queue
        curr = queue.get()
        print(curr)
        if whatToFind == curr:
            print('found!')
            return#we have found what we are looking for
        if curr in graph:#if the current node has adjacent nodes
            [queue.put(adjacent) for adjacent in graph[curr]]#add next nodes into queue

def DFS(graph, root):
    stack = []
    visited = []

    stack.extend(root)

    while(stack):
        outputFromStack = stack.pop()
        visited.extend(outputFromStack)
        #print(outputFromStack)
        inputToStack = list(set(graph[outputFromStack]) - set(visited))
        inputToStack.sort()
        stack.extend(inputToStack)

    return visited

            
N, M, V = map(int, input().split()); matrix=[]; DictKey=[]
for i in range(M):
    matrix.append(list(map(int, input().split())))
for i in range(len(matrix)):
    DictKey.append(matrix[i][0])
Adjacency={k: [] for k in set(DictKey)}
for i in range(len(matrix)):
    Adjacency[matrix[i][0]].append(matrix[i][1])

print(DFS(Adjacency, 1))
bfs(Adjacency, 1, 4)
