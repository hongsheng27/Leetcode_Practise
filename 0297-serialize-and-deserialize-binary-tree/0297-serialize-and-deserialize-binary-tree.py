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
        def dfs(node, path):
            if not node: 
                path.append("N")
                return
            path.append(str(node.val))
            dfs(node.left, path)
            dfs(node.right, path) 

            return path
        
        res = dfs(root, [])
        return ",".join(dfs(root, []))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')
        def dfs(i):
            if data[i] == "N": 
                return None, i + 1
            head = TreeNode(data[i])
            head.left, nextIndex = dfs(i + 1)
            head.right, nextIndex = dfs(nextIndex)
            return head, nextIndex
        return dfs(0)[0]
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))