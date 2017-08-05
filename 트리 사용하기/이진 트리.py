import string
c=0
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        global c
        c+=1
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                    l.append(c)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right= Node(data)
                    l.append(c)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            l.append(c)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def print_l(self):
        print(l)

l=[]
n=int(input())
root=Node(int(input()))
for i in range(n-1):
    root.insert(int(input()))
root.print_l()
# root.print_tree()
