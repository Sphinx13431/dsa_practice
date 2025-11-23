# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder_list=list()
    
    def inorder(self,root:Optional[TreeNode])->None:
        if not root:
            return None
        self.inorder(root.left)
        self.inorder_list.append(root.val)
        self.inorder(root.right)
    
    def two_sum(self, arr: List[int], k: int) -> bool:
        seen = set()
        for ele in arr:
            if k - ele in seen:
                return True
            seen.add(ele)
        return False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.inorder(root)
        return self.two_sum(self.inorder_list,k)