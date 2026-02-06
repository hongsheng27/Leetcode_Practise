# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxDiff = 0
        def dfs(node):
            if not node: return 0
        
            left = dfs(node.left)
            right = dfs(node.right)
            self.maxDiff = max(self.maxDiff, abs(left - right))
               
            return 1 + max(left, right)
        dfs(root)
        return True if self.maxDiff <= 1 else False




            
        return True if self.maxDiff <= 1 else False
       