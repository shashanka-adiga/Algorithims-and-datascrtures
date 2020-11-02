from  collections import defaultdict
class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def horizontal_distance(root, maximum, minimum, hd):
    if root is None:
        return
    if hd > maximum[0]:
        maximum[0] = hd
    if hd <  minimum[0]:
        minimum[0] = hd
    horizontal_distance(root.left, maximum, minimum, hd-1)
    horizontal_distance(root.right, maximum, minimum, hd + 1)

def store_list(root, line_no, hd, table):
    if root is None:
        return
    if line_no == hd:
        table[line_no].append(root.val)
    store_list(root.left, line_no, hd-1, table)
    store_list(root.right, line_no, hd+1, table)

def bottom_view(root):
    maximum = [0]
    minimum = [0]
    hd = 0
    horizontal_distance(root, maximum, minimum, hd)
    table = defaultdict(list)
    for line_no in range(minimum[0], maximum[0]+1):
        store_list(root, line_no, 0, table)
    for i in table:
        print(table[i].pop(),end=' ')

t = Tree(1)
t.right = Tree(2)
t.right.right = Tree(4)
t.right.right.left = Tree(3)
t.right.right.right = Tree(5)
bottom_view(t)