# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def is_mirror(self,p:Optional[TreeNode],q:Optional[TreeNode])->bool:
        if not p and not q:
            return True
        if (not p and q) or (not q and p):
            return False
        if p.val!=q.val:
            return False
        return self.is_mirror(p.left,q.right) and self.is_mirror(p.right,q.left)   

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_mirror(root.left,root.right)