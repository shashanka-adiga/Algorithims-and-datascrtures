class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def height(root):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left),height(root.right))


def solution(root):
    h = height(root)
    ltr = True
    for lvl in range(1, h+1):
        print_level(root, lvl, ltr)
        ltr = not ltr

def print_level(root, lvl, ltr):
    if root is None:
        return
    if lvl == 1:
        print(root.val, end=' ')
        return

    if ltr:
        print_level(root.left, lvl-1,ltr)
        print_level(root.right, lvl-1, ltr)
    else:
        print_level(root.right, lvl - 1, ltr)
        print_level(root.left, lvl - 1, ltr)



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
solution(t)
















# from collections import defaultdict
# class Tree:
#     def __init__(self, key):
#         self.val = key
#         self.left = None
#         self.right = None
#
# def height(root):
#     if root is None:
#         return 0
#     return 1 + max(height(root.left), height(root.right))
#
# def spiral_lvl_order(root, lvl, lvl_order, vd):
#     if root is None:
#         return
#     if vd == lvl:
#         lvl_order[lvl].append(root.val)
#     spiral_lvl_order(root.left, lvl, lvl_order, vd+1)
#     spiral_lvl_order(root.right, lvl, lvl_order, vd+1)
#
#
# def solution(root):
#     lvl_order = defaultdict(list)
#     h = height(root)
#     for lvl in range(1, h+1):
#         spiral_lvl_order(root, lvl, lvl_order, 1 )
#     print(lvl_order)
#     for key,val in lvl_order.items():
#         if key == 1:
#             print(val[0],end=' ')
#         elif key % 2 == 0:
#             val.reverse()
#             for i in val:
#                 print(i,end=' ')
#         else:
#             for i in val:
#                 print(i,end=' ')