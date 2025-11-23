class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)
        return max(leftHeight,rightHeight)+1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        return abs(left-right)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)