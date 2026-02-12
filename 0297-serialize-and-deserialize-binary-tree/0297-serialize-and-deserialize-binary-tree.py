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
        res = []
        def dfs(node):
            if not node:
                return res.append('N')
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        self.index= 0
        def dfs():
            if data[self.index] == "N": return None
            head = TreeNode(str(data[self.index]))
            self.index += 1
            head.left = dfs()
            self.index += 1
            head.right = dfs()
            return head
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))