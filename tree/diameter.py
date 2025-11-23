class Solution:

    def __init__(self):
        self.max_diameter=0

    def maxDepth(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        leftHeight=self.maxDepth(root.left)
        rightHeight=self.maxDepth(root.right)
        self.max_diameter=max(leftHeight+rightHeight,self.max_diameter)
        return max(leftHeight,rightHeight)+1 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        val=self.maxDepth(root)
        return self.max_diameter