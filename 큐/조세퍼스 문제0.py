from collections import deque

class Queue:
    def __init__(self, initValue=[]):
        self.q = deque(initValue)

    def isEmpty(self):
        return len(self.q) == 0

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.popleft()

    def size(self):
        return len(self.q)


def joseph(m, n):
    q = Queue(range(1,m+1))
    print('<', end='')
    while q.size() > 1:
        for i in range(n-1):
            q.enqueue(q.dequeue())
        print(q.dequeue(), end=", ")
    print(q.dequeue(), end='')
    print('>')
    

def main():
    n,m=map(int,input().split())
    joseph(n,m)

if __name__ == "__main__":
    main()