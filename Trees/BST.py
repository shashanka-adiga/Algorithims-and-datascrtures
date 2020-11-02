class BinarySearchTree:
    def __init__(self, key):
        self.val = key
        self.right = None
        self.left = None

def insert(root, key):
   if root is None:
       return

   elif key < root.val :
       if root.left is None:
           root.left = BinarySearchTree(key)
       else:
            insert(root.left, key)
   else:
       if root.right is None:
           root.right = BinarySearchTree(key)
       else:
            insert(root.right, key)


   # elif root.left is None and key < root.val:
   #     root.left = BinarySearchTree(key)
   #
   # elif root.right is None and key > root.val:
   #     root.right = BinarySearchTree(key)
   #
   # else:
   #     insert(root.left, key)
   #     insert(root.right, key)

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)

root = BinarySearchTree(10)
root.left = BinarySearchTree(6)
root.right = BinarySearchTree(12)
insert(root, 14)
insert(root, 8)
print_tree(root)