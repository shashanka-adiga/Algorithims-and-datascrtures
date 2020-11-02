class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_width(root, maximum, minimum, hd):
    if root is None:
        return
    if hd > maximum[0]:
        maximum[0] = hd
    if hd < minimum[0]:
        minimum[0] = hd
    find_width(root.left, maximum, minimum, hd-1)
    find_width(root.right, maximum, minimum, hd+1)

def width(root):
    if root is None:
        return "tree is empty"
    maximum = [0]
    minimum = [0]
    hd = 0
    find_width(root, maximum, minimum, hd)
    print(maximum[0]+abs(minimum[0]))

root = Tree(10)
root.left = Tree(8)
root.right = Tree(12)
root.left.left = Tree(6)
root.left.right = Tree(7)
root.left.right.left = Tree(80)
root.left.right.left = Tree(90)
root.left.right.left.left = Tree(100)
root.left.right.left.left.left = Tree(110)
root.right.right = Tree(14)
root.right.left = Tree(13)
width(root)