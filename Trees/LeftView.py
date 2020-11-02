from collections import defaultdict
left_v = defaultdict(list)
class Tree:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))


def left_view(root):
  h = height(root)
  for lvl in range(1, h+1):
      print_level(root, lvl, 1)
  print("left view:",end='')
  for i in left_v:
      print(left_v[i][0], end=' ')

def print_level(root, lvl, vd):
    if root is None:
        return
    if lvl == vd:
        left_v[vd].append(root.val)
        return
    print_level(root.left, lvl, vd+1)
    print_level(root.right, lvl, vd+1)

t = Tree(1)
t.left = Tree(3)
t.right = Tree(5)
t.left.left = Tree(8)
t.left.right = Tree(9)
t.right.left = Tree(10)
t.right.right = Tree(14)
t.right.right.left = Tree(6)
left_view(t)