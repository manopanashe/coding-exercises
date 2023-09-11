class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    if root is None:
        return True
    
    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) <= 1 and is_balanced(root.left) and is_balanced(root.right):
        return True
    
    return False
    
def height(node):
    if node is None:
        return 0
    
    left_height = height(node.left)
    right_height = height(node.right)


    return max(left_height,right_height) + 1

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

print(is_balanced(root))

