class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            # Both p and q are smaller → go left
            if p.val < root.val and q.val < root.val:
                root = root.left
            
            # Both p and q are greater → go right
            elif p.val > root.val and q.val > root.val:
                root = root.right
            
            # Split point → this is the LCA
            else:
                return root
