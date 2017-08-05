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
            self.left.inorder()
        print(self.data)
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data)

def main():
    figure=int(input())
    matrix=[]
    while True:
        line=input()
        if not line: break
        values=line.split()
        row=[str(value) for value in values]
        matrix.append(row)

    # print(matrix[0][1])
    # print(len(matrix))
    root=Node(matrix[0][0])
    for i in range(figure):
        for j in range(3):
            root.insert(matrix[i][j])

    print('inorder Traversal...')
    root.inorder()
    print('preorder Traversal...')
    root.preorder()
    print('postorder Traversal...')
    root.postorder()
'''
def main():
    root=Node(8)
    root.insert(3)
    root.insert(1)
    root.insert(6)
    root.insert(7)
    root.insert(10)
    root.insert(14)
    root.insert(13)
    print(root)
    print('inorder Traversal...')
    root.inorder()
    print('preorder Traversal...')
    root.preorder()
    print('postorder Traversal...')
    root.postorder()
'''

if __name__ == '__main__':
    main()
