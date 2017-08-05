def push(number) :
    list.append(number)
def pop() :
    if not list:
        print('-1')
    else:
        #list.pop(0)
        print(list.pop(0))
def size() :
    print(len(list))
def empty() :
    if not list:
        print('1')
    else:
        print('0')
def front() :
    if not list:
        print('-1')
    else:
        print(list[0])
def back() :
    if not list:
        print('-1')
    else:
        print(list[len(list)-1])

N = int(input())
list = []

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
    elif command[0] == 'front':
         front()
    elif command[0] == 'back':
         back()
