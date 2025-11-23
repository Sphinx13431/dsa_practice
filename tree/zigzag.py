# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        queue=deque()
        queue.append([root])
        result=list()
        r2l=0
        while queue:
            nodeList=queue.popleft()
            if r2l==1:
                length=len(nodeList)
                rev=[]
                for i in range(length-1,-1,-1):
                    rev.append(nodeList[i].val)
                result.append(rev)
                r2l=0
            else:
                result.append([node.val for node in nodeList])
                r2l=1
            tempList=[]
            for node in nodeList:
                if node.left:
                    tempList.append(node.left)
                if node.right:
                    tempList.append(node.right)
            if tempList:
                queue.append(tempList)
        return result