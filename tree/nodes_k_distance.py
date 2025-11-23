# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.parent=dict()
        self.visited=set()

    def bfs(self,root:TreeNode):
        q=deque()
        q.append([root])
        self.parent[root]=None
        while q:
            nodeList=q.popleft()
            temp=list()
            for node in nodeList:
                if node.left:
                    self.parent[node.left]=node
                    temp.append(node.left)
                if node.right:
                    self.parent[node.right]=node
                    temp.append(node.right)
            if temp:
                q.append(temp)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.bfs(root)
        q=deque()
        q.append([target])
        self.visited.add(target)
        while q:
            nodeList=q.popleft()
            if k==0:
                return [node.val for node in nodeList]
            temp=list()
            for node in nodeList:
                parentNode,left,right=self.parent[node],node.left,node.right
                if parentNode and parentNode not in self.visited:
                    temp.append(parentNode)
                    self.visited.add(parentNode)
                if left and left not in self.visited:
                    temp.append(left)
                    self.visited.add(left)
                if right and right not in self.visited:
                    temp.append(right)
                    self.visited.add(right)
            if temp:
                k-=1
                q.append(temp)
        return list()