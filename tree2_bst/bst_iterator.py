# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder_list=list()
        self.inorder_traversal(root)
        self.ptr=-1
        self.length=len(self.inorder_list)      
    def inorder_traversal(self,root:Optional[TreeNode]):
        if (not root):
            return
        self.inorder_traversal(root.left)
        self.inorder_list.append(root.val)
        self.inorder_traversal(root.right)

    def next(self) -> int:
        self.ptr+=1
        return self.inorder_list[self.ptr]

    def hasNext(self) -> bool:
        return self.ptr+1<self.length
