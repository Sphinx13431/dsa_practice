# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    
class Solution:
    def deleteNode(self, root, key):
        if not root:
            return None
        
        # search
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        
        # now root.val == key → delete this node

        # Case 1: no child
        if not root.left and not root.right:
            return None
        
        # Case 2: one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        
        # Case 3: two children → find inorder successor
        successor = root.right
        while successor.left:
            successor = successor.left
        
        # replace value
        root.val = successor.val
        
        # delete successor from right subtree
        root.right = self.deleteNode(root.right, successor.val)
        
        return root
