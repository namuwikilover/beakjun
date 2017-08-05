import Queue

def bfs(graph, root, whatToFind):
    queue = Queue.Queue()
    queue.put(root)
    while(queue):
        curr = queue.get()
        print curr
        if whatToFind == curr:
            print('found!')
            return
        if curr in graph:
            [queue.put(adjacent)] for adjacent in graph[curr]]
