class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mini,maxi=0,0
        result=[]
        column_dict=defaultdict(list)
        queue=deque()
        queue.append([root,0,0])


        while queue:
            node,row,col=queue.popleft()
            column_dict[col].append((row, node.val))
            if node.left:
                queue.append([node.left,row+1,col-1])
                mini=min(mini,col-1)
            if node.right:
                queue.append([node.right,row+1,col+1])
                maxi=max(maxi,col+1)
        for col in range(mini, maxi + 1):
            # Sort first by row, then by value
            column_nodes = sorted(column_dict[col], key=lambda x: x[0])
            result.append([val for row, val in column_nodes])
            
        return result