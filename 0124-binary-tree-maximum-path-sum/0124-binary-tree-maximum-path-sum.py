# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (0, float('-inf')) # pathSum, largestSum
            leftGain, leftMaxSum = dfs(node.left)
            rightGain, rightMaxSum = dfs(node.right)

            leftGain = max(0, leftGain)
            rightGain = max(0, rightGain)

            largestSum = node.val + leftGain + rightGain
            
            return (node.val + max(leftGain, rightGain), max(largestSum, leftMaxSum, rightMaxSum))
        return dfs(root)[1]
        