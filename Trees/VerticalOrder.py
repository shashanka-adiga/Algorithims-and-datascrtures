class Tree:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None
def range_of_tree(root, maximum, minimum, hd):
    if root is None:
        return 0
    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    range_of_tree(root.left, maximum, minimum, hd-1)
    range_of_tree(root.right, maximum, minimum, hd+1)

def print_vertical_order(root, line_no, hd):
    if root is None:
        return 0
    if hd == line_no:
        print(root.val,end=' ')
    print_vertical_order(root.left, line_no, hd-1)
    print_vertical_order(root.right, line_no, hd+1)

def vertical_order(root):
    if root is None:
        return "Tree is empty"
    maximum = [0]
    minimum = [0]
    range_of_tree(root, maximum, minimum, 0)
    for line_no in range(minimum[0], maximum[0]+1):
        print_vertical_order(root, line_no, 0)

t = Tree(1)
t.left = Tree(3)
t.right = Tree(5)
t.left.left = Tree(8)
t.left.right = Tree(9)
t.right.left = Tree(10)
t.right.right = Tree(14)
vertical_order(t)

