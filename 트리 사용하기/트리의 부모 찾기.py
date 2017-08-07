N=int(input());matrix=[]; DictKey=[] # 입력 형식 받기

for i in range(N-1):
    matrix.append(list(map(int, input().split())))

for i in range(len(matrix)):
    DictKey.append(matrix[i][0])
for i in range(len(matrix)):
    DictKey.append(matrix[i][1]) # 이까지 그래프 딕셔너리 키 생성

Graph={k: [] for k in set(DictKey)} # 그래프 딕셔너리 생성
for i in range(len(matrix)):    # 그래프 자료 입력
    Graph[matrix[i][0]].append(matrix[i][1])

for parent, child in Graph.items():
    print(parent, child)