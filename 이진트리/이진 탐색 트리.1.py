class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.looup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
                return self.right.looup(data, self)
        else:
            return self, parent

    def inorder(self):
        if self.left:
            self.left.inorder
        print(self.data)
        if self.right:
            self.right.inorder

def main():
    root=Node(0)                #generate tree....
    number=int(input())
    input_number=[]
    for i in range(number):
        input_number.append(input())
        root.insert(input_number[i])
        root.inorder()

if __name__ == '__main__':
    main()
