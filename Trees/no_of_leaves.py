class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def no_of_leaves(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return no_of_leaves(root.left) + no_of_leaves(root.right)


root = Tree(10)
root.left = Tree(8)
root.left.left = Tree(7)
root.left.right = Tree(6)
root.right = Tree(9)
print(no_of_leaves(root))