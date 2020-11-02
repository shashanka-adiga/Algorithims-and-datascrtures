class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def has_path_sum(root, sm):
    if root is None:
        return False
    else:
        ans = False
        subsum = sm - root.val
        if subsum == 0 and root.left is None and root.right is None:
            return True
        ans = ans or has_path_sum(root.left, subsum) or has_path_sum(root.right, subsum)
        return ans

root = Tree(10)
root.left = Tree(8)
root.right = Tree(12)
root.left.left = Tree(6)
root.left.right = Tree(7)
root.right.right = Tree(14)
root.right.left = Tree(13)
print(has_path_sum(root, 36))