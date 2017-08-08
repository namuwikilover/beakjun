class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children

    def print_tree(self):
        print(self.val)
        if self.leftChild:
            self.leftChild.print_tree()
        if self.rightChild:
            self.rightChild.print_tree()

    def find_tree(self, val):
        if(currentNode is None):
            return False
        if(val == currentNode.val):
            print(self.val)
        if self.leftChild:
            self.leftChild.print_tree()
        if self.rightChild:
            self.rightChild.print_tree()
            
        
class BST:
    
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val):
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

# Make binary search tree
bst = BST()

# Insert value
N=int(input()); level=1

# make level
for i in range(N):
    level *= 2

for i in range(1, level+1):
    bst.insert(i)

# Print tree
bst.root.print_tree()


 