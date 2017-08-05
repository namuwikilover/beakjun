def push(number) :
    li.append(number)
def pop() :
    if not li :
        print('-1')
    else:
        print(li.pop())
def size() :
    print(len(li))
def empty() :
    if not li :
        print(1)
    else :
        print(0)
def top() :
    if len(li)-1>=0:
        print(li[len(li)-1])
    else:
        print('-1')
N = int(input())
li = []

for i in range(N):
    command = input().split()
    if command[0] == 'push' :
        push(command[1])
    elif command[0] == 'pop' :
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
         empty()
    elif command[0] == 'top':
         top()
