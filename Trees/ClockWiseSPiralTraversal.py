class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left),height(root.right))

def solution(root):
    h = height(root)
    ptr = True
    start = 1
    end = h
    print("clock wise spiral traversal:",end=' ')
    for i in range(h):
        if ptr:
            print_level(root, start, ptr)
            ptr = not ptr
            start = start + 1
        else:
            print_level(root, end, ptr)
            ptr = not ptr
            end = end - 1

def print_level(root, lvl, ptr):
    if root is None:
        return
    if lvl == 1:
        print(root.val, end=' ')
        return

    if ptr:
        print_level(root.left, lvl-1, ptr)
        print_level(root.right, lvl-1, ptr)
    else:
        print_level(root.right, lvl - 1, ptr)
        print_level(root.left, lvl - 1, ptr)


root = Tree(10)
root.right = Tree(9)
root.right.right = Tree(14)
root.right.right.left = Tree(21)
root.right.right.right = Tree(20)
root.right.left = Tree(15)
root.right.left.right = Tree(22)
root.right.left.left = Tree(23)
root.left = Tree(8)
root.left.left = Tree(17)
root.left.left.right = Tree(26)
root.left.left.left = Tree(27)
root.left.right = Tree(16)
root.left.right.right = Tree(24)
root.left.right.left = Tree(25)
solution(root)






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
#     else:
#         return max(1+height(root.left), 1+height(root.right))
#
# def store(root, vert_dist, vd, table):
#     if root is None:
#         return
#     if vert_dist == vd:
#         table[vert_dist].append(root.val)
#     store(root.left, vert_dist+1, vd, table)
#     store(root.right,vert_dist+1, vd, table)
#
# def trav_order(tree_height):
#     i = 1
#     j = tree_height
#     to = []
#     while i <= (tree_height+1)//2:
#         to.append(i)
#         if j not in to:
#             to.append(j)
#         i+=1
#         j-=1
#     return to
#
# def forward_order(tree_height):
#     i = 1
#     fwd = []
#     while i <= (tree_height+1)//2:
#         fwd.append(i)
#         i+=1
#     return  fwd
#
# def backward_order(tree_height):
#     i = tree_height
#     bck = []
#     while i > (tree_height+1)//2:
#         bck.append(i)
#         i-=1
#     return  bck
#
# def level_order(root):
#     if root is None:
#         return "Tree is empty"
#     height_of_tree = height(root)
#     order = trav_order(height_of_tree)
#     for_ord = forward_order(height_of_tree)
#     bck_ord = backward_order(height_of_tree)
#     vert_dist = 1
#     table = defaultdict(list)
#     for vd in range(1, height_of_tree+1):
#         store(root, vert_dist, vd, table)
#     for i in order:
#         if i in for_ord:
#             for elem in table[i]:
#                 print(elem,end=' ')
#         else:
#             for elem in reversed(table[i]):
#                 print(elem,end=' ')

