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
        if not root: return ""
        self.res = ""
        def dfs(node):
            if not node:
                self.res += '#,'
                return
            self.res += str(node.val) + ','
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.res[:-1]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        self.index = 0
        def dfs():
            # base case
            if data[self.index] == '#': 
                return None
            # recursion case
            node = TreeNode(int(data[self.index]))
            self.index += 1
            node.left = dfs()
            self.index += 1
            node.right = dfs()
            return node
        return dfs()



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))