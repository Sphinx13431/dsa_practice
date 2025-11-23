# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q=deque()
        maxWidth=1
        q.append([[root,0]])#here the queue stores node and index

        while q:
            node_details=q.popleft()
            length=len(node_details)
            left_index,right_index=node_details[0][1],node_details[length-1][1]
            maxWidth=max(maxWidth,right_index-left_index+1)
            temp_list=list()
            for i in range(length):
                node,index=node_details[i]
                if node.left:
                    temp_list.append([node.left,2*index])
                if node.right:
                    temp_list.append([node.right,2*index+1])
            if temp_list:
                q.append(temp_list)
        return maxWidth