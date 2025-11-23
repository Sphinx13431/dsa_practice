# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]

        for value in preorder[1:]:
            if value < stack[-1].val:
                newNode = TreeNode(value)
                stack[-1].left = newNode
                stack.append(newNode)
            else:
                temp = None
                while stack and value > stack[-1].val:
                    temp = stack.pop()

                newNode = TreeNode(value)
                temp.right = newNode
                stack.append(newNode)

        return root
