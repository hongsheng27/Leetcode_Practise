# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, lower):
            # base case
            if not node: return 0
            # recursion case
            left = dfs(node.left, max(node.val, lower))
            right = dfs(node.right, max(node.val, lower))
            isGood = 1 if node.val >= lower else 0
            return left + right + isGood
        return dfs(root, root.val)