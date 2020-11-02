class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def divergent_left(root, div_left):
    queque = [root]
    while queque:
        node = queque.pop(0)
        if node.left and node.right:
            div_left[node.val] = abs(node.left.val - node.right.val)
            queque.append(node.left)
            queque.append(node.right)
        elif node.left and node.right is None:
            div_left[node.val] = node.left.val
            queque.append(node.left)
        elif node.left is None and node.right:
            div_left[node.val] = node.right.val
            queque.append(node.right)
        else:
            div_left[node.val] = 0

def divergent_right(root, div_right):
    queque = [root]
    while queque:
        node = queque.pop(0)
        if node.left and node.right:
            div_right[node.val] = abs(node.left.val - node.right.val)
            queque.append(node.left)
            queque.append(node.right)

        elif node.left and node.right is None:
            div_right[node.val] = node.left.val
            queque.append(node.left)
        elif node.left is None and node.right :
            div_right[node.val] = node.right.val
            queque.append(node.right)
        else:
            div_right[node.val] = 0

def divergent(root):
    if root.left is None and root.right is None:
        return 0
    left_sum = 0
    right_sum = 0
    div_left = {}
    div_right = {}
    divergent_left(root.left, div_left)
    for key,val in div_left.items():
        left_sum = left_sum + val
    divergent_right(root.right, div_right)
    for key,val in div_right.items():
        right_sum = right_sum + val
    print(div_left)
    print(div_right)
    print("divergent of tree:",abs(left_sum-right_sum))

t = Tree(1)
t.left = Tree(7)
t.left.left = Tree(9)
t.left.right = Tree(8)
t.left.right.left = Tree(10)
t.left.right.left.left = Tree(12)
t.left.right.left.left.left = Tree(14)
t.right = Tree(2)
t.right.right = Tree(4)
t.right.right.left = Tree(3)
t.right.right.right = Tree(5)
divergent(t)