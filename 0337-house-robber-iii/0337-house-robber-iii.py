# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:
        def dfs(node):
            if not node: return (0, 0)

            dp = dfs(node.left)
            dp2 = dfs(node.right)

            # (rob_current, skip_current)
            return (dp[1] + dp2[1] + node.val, max(dp[0], dp[1]) + max(dp2[0], dp2[1]))
        res = dfs(root)
        return max(res[0], res[1])
        