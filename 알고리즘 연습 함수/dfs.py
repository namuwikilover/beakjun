def dfs(graph, root, whatToFind):
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr)
        if whatToFind == curr:
            print('found!')
            return
        if curr in graph:
            [stack.append(adjacent) for adjacent in graph[curr]]
