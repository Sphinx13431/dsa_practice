class Solution:
    def dfs(self,root:Optional[TreeNode],val:int)->Optional[TreeNode]:
        if not root.left and not root.right:
            return root
        if root.left.val < val:
            return self.dfs(root.right,val)
        return self.dfs(root.left,val)
        
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        node=self.dfs(root,val)
        node_value=node.val
        if node_value>val:
            node.right=TreeNode(val)
        else:
            node.left=TreeNode(val)
        return root