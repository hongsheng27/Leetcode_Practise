# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (0, float('-inf')) # pathSum, ans
            leftSum, leftAns  = dfs(node.left)
            rigthSum, rightAns = dfs(node.right)

            ans = node.val + max(0, leftSum) + max(0, rigthSum)
            
            return (node.val + max(leftSum, rigthSum, 0), max(ans, leftAns, rightAns))
        return dfs(root)[1]
        