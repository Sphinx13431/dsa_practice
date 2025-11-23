class Solution:
    def __init__(self):
        self.preorder_list=list()

    def inorder(self,root):
        if not root:
            return None
        self.inorder(root.left)
        self.preorder_list.append(root.val)
        self.inorder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        return self.preorder_list[k-1]
        