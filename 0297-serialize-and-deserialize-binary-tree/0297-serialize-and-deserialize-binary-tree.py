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
        res = [] # i.g. [1, 2, n, n, 3, 4, n ,n , 5, n, n]
        def dfs(node):
            if not node: 
                res.append('n')
                return
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
        self.index = 0
        def dfs():
            val = data[self.index]
            self.index += 1
            # base case
            if val == 'n': return None
            # recursion case
            head = TreeNode(val)
            head.left = dfs()
            head.right = dfs()
            return head
        return dfs()
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))