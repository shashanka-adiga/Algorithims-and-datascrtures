# class Tree:
#     def __init__(self, key):
#         self.right = None
#         self.left = None
#         self.val = key
#
# def invert(root):
#     if root is None:
#         return
#     else:
#         invert(root.left)
#         invert(root.right)
#     root.left , root.right = root.right , root.left
#
# def inorder(root):
#     if root is None:
#         return
#     else:
#         inorder(root.left)
#         print(root.val, end=' ')
#         inorder(root.right)
#
# root = Tree(10)
# root.left = Tree(7)
# root.left.left = Tree(12)
# root.left.right = Tree(13)
# root.right = Tree(6)
# root.right.left = Tree(4)
# root.right.right = Tree(5)
# inorder(root)
# print('')
# invert(root)
# inorder(root)
