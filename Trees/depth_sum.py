class Tree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def depth_sum(root, sum_depth, depth, visited):
    if root:
        if not visited[root.val] :
            sum_depth[0] = sum_depth[0] + depth
            visited[root.val] = True
        depth_sum(root.left, sum_depth, depth+1, visited)
        depth_sum(root.right, sum_depth, depth + 1, visited)

def initialize(root, visited):
    if root:
        visited[root.val] = False
        initialize(root.left, visited)
        print(root.val, end=' ')
        initialize(root.right, visited)

def summ(root):
    if root is None:
        return
    visited = {}
    initialize(root, visited)
    sum_depth = [0]
    depth_sum(root, sum_depth, 0, visited)
    print()
    print('sum of depth of all node:',end=' ')
    print(sum_depth[0])

root = Tree('A')
root.left = Tree('B')
root.left.left = Tree('C')
root.left.right = Tree('D')
root.right = Tree('E')
root.right.right = Tree('F')
root.right.left = Tree('G')
summ(root)
