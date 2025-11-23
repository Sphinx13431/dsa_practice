from typing import Optional,List
class TreeNode:
    def __init__(self,val:0,left:None,right:None):
        self.val=val
        self.left,self.right=left,right

class Preorder:
    def __init__(self):
        self.preorder=[]

    def traverse(self,root:Optional[TreeNode]):
        if not root:
            return None
        self.preorder.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.preorder
    
class Inorder:
    def __init__(self):
        self.inorder=[]

    def traverse(self,root:Optional[TreeNode]):
        if not root:
            return None
        
        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.inorder

class Postorder:
    def __init__(self):
        self.postorder=[]

    def traverse(self,root:Optional[TreeNode]):
        if not root:
            return None
        
        self.traverse(root.left)
        self.traverse(root.right)
        self.postorder.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.traverse(root)
        return self.postorder