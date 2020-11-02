class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def is_siblings(root, value1, value2):
    if root is None:
        return
    else:
        return (root.left == value1 and root.right == value2) or (root.left == value2 and root.right == value1) or is_siblings(root.left, value1, value2) or is_siblings(root.right, value1, value2)
def level(root, value, lvl):
    if root is None:
        return 0
    if root.val == value:
        return lvl
    else:
        l = level(root.left, value, lvl + 1) or level(root.right, value, lvl + 1)
        return l


def is_cousin(root, value1, value2):
    if root is None:
        return
    print('level of first node:',level(root, value1.val, 1))
    print('level of second node:',level(root, value2.val, 1))
    print('siblings?',is_siblings(root, value1, value2))
    if level(root, value1.val, 1) == level(root, value2.val, 1) and (not is_siblings(root, value1, value2)):
        print('they are cousins!')
    else:
        print('they are not cousins')

t = Tree(1)
t.left = Tree(3)
t.right = Tree(5)
t.left.left = Tree(8)
t.left.right = Tree(9)
t.right.left = Tree(10)
t.right.right = Tree(14)
is_cousin(t, t.right.left, t.left.left)

