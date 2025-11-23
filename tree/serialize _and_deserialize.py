# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q=deque()
        result=''
        q.append(root)
        while q:
            node=q.popleft()
            if not node:
                result+='#,'
            else:
                result+=str(node.val)+','
                q.append(node.left)
                q.append(node.right)
        return result

    def deserialize(self, data):
        if not data:
            return None

        vals = data.split(',')
        if vals[0] == '#':
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])

        i = 1
        while q and i < len(vals):
            node = q.popleft()

            # Left child
            if vals[i] != '#':
                leftNode = TreeNode(int(vals[i]))
                node.left = leftNode
                q.append(leftNode)
            i += 1

            # Right child
            if i < len(vals) and vals[i] != '#':
                rightNode = TreeNode(int(vals[i]))
                node.right = rightNode
                q.append(rightNode)
            i += 1

        return root