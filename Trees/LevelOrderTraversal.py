class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def level_traversal(root):
    if root is None:
        return
    queue = [root]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val,end=' ')
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

t = Tree(1)
t.left = Tree(3)
t.right = Tree(5)
t.left.left = Tree(8)
t.left.right = Tree(9)
t.right.left = Tree(10)
t.right.right = Tree(14)
level_traversal(t)
