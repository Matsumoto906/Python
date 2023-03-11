class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False
        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def find(self, data):
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
            print(str(self.data), end = ' ')
            
class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def post_order(self):
        print()
        if self.root is not None:
            self.root.post_order()


for t in range(int(input())):
    tree=Tree()
    s=int(input())
    num=list(map(int,input().split(',')))
    for i in num:
        tree.insert(i)
    tree.post_order()