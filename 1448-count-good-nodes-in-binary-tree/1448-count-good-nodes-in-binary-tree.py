# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
   
        def dfs(node, rootVal):
            if not node: return 0
            isGood = 0
            if node.val >= rootVal: isGood += 1    
            rootVal = max(node.val, rootVal)  
            return isGood + dfs(node.left, rootVal) + dfs(node.right, rootVal)
        return dfs(root, root.val)
 
        