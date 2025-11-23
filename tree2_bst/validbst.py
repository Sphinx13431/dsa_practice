# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self,root:Optional[TreeNode],low:int,high:int)->bool:
        if not root:
            return True
        if not(low<root.val<high):
            return False
        return self.validate(root.left,low,root.val) and self.validate(root.right,root.val,high)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.validate(root,-1*sys.maxsize,sys.maxsize)