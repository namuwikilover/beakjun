import timeit
import sys
def BFS(start, target, GRAPH):
    queue = [start]
    visited = []

    while len(queue) > 0:
        if len(queue)==0: break
        x = queue.pop(0)

        # if x == target:
        #     visited.append(x)
        #     return visited
        if x not in visited:
            visited = visited+[x]
        if len(GRAPH[x])>0:
            queue = queue + GRAPH[x]
        else:
            continue

    return visited

N=int(sys.stdin.readline()[:-1]); M=int(sys.stdin.readline()[:-1]); matrix=[]; DictKey=[]
start=timeit.default_timer()
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline()[:-1].split())))
# print(matrix)
for i in range(len(matrix)):
    DictKey.append(matrix[i][0])
for i in range(len(matrix)):
    DictKey.append(matrix[i][1])
# print(set(DictKey))
Graph={k: [] for k in set(DictKey)}
for i in range(len(matrix)):
    Graph[matrix[i][0]].append(matrix[i][1])

print(len(BFS(1, 4, Graph))-1)
stop=timeit.default_timer()
# print(stop-start)

