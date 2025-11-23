class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)
        return max(leftHeight,rightHeight)+1