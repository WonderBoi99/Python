class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left == None:
                self.left = BinaryTreeNode(data)
            else:
                self.left.add_child(data)
        else:
            if self.right == None:
                self.right = BinaryTreeNode(data)
            else:
                self.right.add_child(data)

    def search(self, val):
        if val == self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


    def in_order_traversal(self):
        e = []
        if self.left:
            e += self.left.in_order_traversal()
        
        e.append(self.data)

        if self.right:
            e += self.right.in_order_traversal()

        return e
    
def build_tree(values):
    root = BinaryTreeNode(values[0])
    for val in range(1,len(values)):
        root.add_child(values[val])
    return root
    
if __name__ == '__main__':
    test = build_tree([15,12,7,14,27,20,88,23])
    print(test.in_order_traversal())
    print(test.search(15))
        
        
