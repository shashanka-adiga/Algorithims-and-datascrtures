class Tree:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key

def ltr_level_order(root):
    if root is None:
        return
    else:
        queue = [root]
        ltr_order = []
        while queue:
            node = queue.pop(0)
            ltr_order.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return ltr_order

def rtl_level_order(root):
    if root is None:
        return
    else:
        queue1 = [root]
        rtl_order = []
        while queue1:
            node = queue1.pop(0)
            rtl_order.append(node.val)
            if node.right is not None:
                queue1.append(node.right)
            if node.left is not None:
                queue1.append(node.left)
    return rtl_order

def is_mirror(root1, root2):
    if ltr_level_order(root1) == rtl_level_order(root2):
        print('mirror images')
    else:
        print('not a mirror image')

    # l1 = ltr_level_order(root1)
    # l2 = rtl_level_order(root2)
    # count = 0
    # i = 0
    # while i < len(l1):
    #     if l1[i] == l2[i]:
    #         count+=1
    #     else:
    #         break
    #     i+=1
    # if count == len(l1):
    #     print('mirror images')
    # else:
    #     print('not a mirror image')

root1 = Tree(1)
root1.left = Tree(2)
root1.right = Tree(3)
root1.left.left = Tree(4)
root1.left.right = Tree(5)
root1.right.left = Tree(6)
root1.right.right = Tree(7)

root2 = Tree(1)
root2.left = Tree(3)
root2.right = Tree(2)
root2.left.left = Tree(7)
root2.left.right = Tree(6)
root2.right.left = Tree(5)
root2.right.right = Tree(4)

is_mirror(root1, root2)