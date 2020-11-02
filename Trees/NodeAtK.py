class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
parent = {}
def node_at_k(root, node, k):
    visited = []
    queue = [node]
    while queue:
        k-=1
        y = queue.pop(0)
        if parent[y] is not None:
            if parent[y] not in visited:
                if k == 0:
                    print(parent[y].val)
                queue.append(parent[y])
                visited.append(parent[y])

        if y.left is not None:
            if y.left not in visited:
                if k == 0:
                    print(y.left.val)
                queue.append(y.left)
                visited.append(y.left)

        if y.right is not None:
            if y.right not in visited:
                if k == 0:
                    print(y.right.val)
                queue.append(y.right)
                visited.append(y.right)

def parent_node(root):
    queue = [root]
    parent[root] = None
    while queue:
        x = queue.pop(0)
        if x.left is not  None:
            parent[x.left] = x
            queue.append(x.left)
        if x.right is not None:
            parent[x.right] = x
            queue.append(x.right)

root = Tree(10)
root.left = Tree(11)
root.left.left = Tree(12)
root.left.left.left = Tree(15)
root.left.right = Tree(13)
root.right = Tree(8)
root.right.right = Tree(7)
root.right.left = Tree(6)
parent_node(root)
node_at_k(root, root.left, 2)