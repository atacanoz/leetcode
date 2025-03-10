# Given the root of a binary tree, invert the tree, and return its root.


class TreeNode: 
    def __init__(self, val = 0, left=None, right= None):
        self.val = val
        self.left = left 
        self.right = right 
    
    def InvertBinaryTree(self, root):      
        while self.left is not None:
            
             