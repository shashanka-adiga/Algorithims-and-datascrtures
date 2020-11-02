
class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

root = Tree(10)
root.left = Tree(8)
root.right = Tree(9)
root.left.left = Tree(6)
root.left.left.left = Tree(4)
print(height(root))


