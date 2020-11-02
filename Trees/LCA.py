class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def path_to(root, value, path):
    if root is None:
        return False
    path.append(root.val)
    if root.val == value:
        return True
    if path_to(root.left, value, path) or path_to(root.right, value, path):
        return True
    return False

def lca(root, value1, value2):
    if root is None:
        return False
    path1 = []
    path2 = []
    if path_to(root, value1,path1) and path_to(root, value2, path2):
        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i = i+1
        print(path1)
        print(path2)
        return path1[i-2]
    return "no common ancestor"

t = Tree(1)
t.left = Tree(3)
t.right = Tree(5)
t.left.left = Tree(8)
t.left.right = Tree(9)
t.right.left = Tree(10)
t.right.right = Tree(14)
print(lca(t, 10, 14))