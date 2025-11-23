class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append([root])
        result = []
        result.append([root.val])  # Store the values, not the nodes

        while queue:
            node_list = queue.popleft()
            child_node_list = []
            child_vals = []  # To store the values at the current level

            for node in node_list:
                if node.left:
                    child_node_list.append(node.left)
                    child_vals.append(node.left.val)
                if node.right:
                    child_node_list.append(node.right)
                    child_vals.append(node.right.val)
            
            if child_node_list:
                result.append(child_vals)
                queue.append(child_node_list)

        return result