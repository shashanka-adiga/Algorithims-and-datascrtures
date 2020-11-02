class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def path_to(root, dest, path):
    if root is None:
        return
    path.append(root.val)
    if root.val == dest:
        print(path)
        exit()
    else:
        path_to(root.left, dest, path)
        path_to(root.right, dest, path)
    path.pop()


# def path_to_node(root, len_path, path, value):
#     if root:
#         if len(path) <= len_path:
#             path.append(root.val)
#         else:
#             path[len_path] = root.val
#         if root.val == value:
#             for i in range(len(path)):
#                 if i == len(path) - 1:
#                     print(path[i])
#                 else:
#                     print(path[i], end=' -> ')
#         len_path+=1
#         path_to_node(root.left, len_path, path, value)
#         path_to_node(root.right, len_path, path, value)
#
# def is_present(root, value):
#     if root is None:
#         return False
#     else:
#         if root.val == value:
#             return True
#         return  is_present(root.left, value) or is_present(root.right, value)
#
#
#
# def path_to(root, value):
#     if root is None:
#         return "Tree is empty"
#     if not is_present(root, value):
#         return "value does not exist"
#     print(is_present(root, value))
#     len_path = 0
#     path = []
#     path_to_node(root, len_path, path, value)

root = Tree(10)
root.left = Tree(8)
root.right = Tree(12)
root.left.left = Tree(6)
root.left.right = Tree(7)
root.right.right = Tree(14)
root.right.left = Tree(13)
path = []
path_to(root, 17, path)