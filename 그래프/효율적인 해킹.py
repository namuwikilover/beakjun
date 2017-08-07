import sys

def BFS(start, target, GRAPH):
    queue = [start]
    visited = []

    while len(queue) > 0:
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

# 입력하는 부분.
N, M=map(int, sys.stdin.readline()[:-1].split()); matrix=[]; DictKey=[]
for i in range(M):
    matrix.append(list(map(int, sys.stdin.readline()[:-1].split())))
for i in range(len(matrix)):
    DictKey.append(matrix[i][0])
for i in range(len(matrix)):
    DictKey.append(matrix[i][1])

# 그래프를 딕셔너리 자료구조를 이용해서 인접 리스트로 표현.
Graph={k: [] for k in set(DictKey)}
for i in range(len(matrix)):
    Graph[matrix[i][1]].append(matrix[i][0])


# BFS를 이용한 그래프 탐색 경로를 출력하고, 각 정점에서 출발한 경로의 길이를 result 리스트에 저장.
result=[]
for i in range(1,6):
    result.append(len(BFS(i, 4, Graph)))

# result 리스트에서 경로가 가장 긴 정점을 출력.
for i in range(len(result)):
    if result[i]==max(result): print(i+1, end=' ')
