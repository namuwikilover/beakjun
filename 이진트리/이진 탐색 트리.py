import sys
c=0; l=[]

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data, i):
        global c
        global l

        if i!=0: c+=1
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    l.append(c)
                else:
                    self.left.insert(data, i)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                    l.append(c)
                else:
                    self.right.insert(data, i)
        else:
            self.data = data

def main():
    root=Node(0)                #generate tree....
    number=int(sys.stdin.readline()[:-1])
    input_number=[]
    for i in range(number):
        if i==0: l.append(0)
        input_number.append(sys.stdin.readline()[:-1])
        root.insert(input_number[i], i)
    for i in range(len(l)):
        print(l[i])
    
if __name__ == '__main__':
    main()
