from node import Node
(_ROOT, _DEPTH, BREADTH) = range(3)
class Tree:
    def __init__(self):
        self.__node = {}
    @property
    def nodes(self):
        return self.__nodes
    def add_node(self, indentifiery, parent=None):
        node=Node(identifier)
        self[indentifier]=node

        if parent is not None:
            self[parent],add_child(identifier)
        return node
    def display(self, identifier, depth=_ROOT):
        children=self[identifier].children
        if depth==_ROOT:
            print("{0}".format(identifier))
        else:
            print("\t"*depth, "{0}".format(identifier))
        depth+=1
        for child in children:
            self.display(child, depth)
    def traversal(self, identifier, mode=_DEPTH):
        queue=self[identifier].children
        while queue:
            yield queue[0]
            expansion=self[queue[0]].children
            if mode==_DEPTH:
                queue=expansion=queue[1:]
            elif mode==_BREADTH:
                queue=queue[1:]+expansion
    def __getitem__(self, key):
        return self.__node[key]
    def __setitem__(self, key, item ):
        self.__nodes[key]=item
