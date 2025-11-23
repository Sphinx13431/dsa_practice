class Solution:
    def __init__(self):
        self.max_sum=-sys.maxsize

    def dfs(self, root:Optional[TreeNode]):

        if not root:
            return 0
        leftsum=max(self.dfs(root.left),0)
        rightsum=max(self.dfs(root.right),0)
        self.max_sum=max(leftsum+rightsum+root.val,self.max_sum)
        return root.val+max(leftsum,rightsum)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.max_sum