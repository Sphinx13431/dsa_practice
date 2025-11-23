class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()
        right_view_list=list()
        right_view_list.append(root.val)
        queue=deque()
        queue.append([root])
        
        while(queue):
            node_list=queue.popleft()
            child_node_list=list()
            for node in node_list:
                right_child=node.right
                left_child=node.left
                if(right_child):
                    child_node_list.append(right_child)
                if(left_child):
                    child_node_list.append(left_child) 
            if child_node_list:
                right_view_list.append(child_node_list[0].val)
                queue.append(child_node_list)

        return right_view_list