# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.maxHeight = 0
        def dfs(node):
            if not node: return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.maxHeight = max(self.maxHeight, abs(left - right))

            return max(left, right) + 1
        dfs(root)
        return True if self.maxHeight <= 1 else False
        
        