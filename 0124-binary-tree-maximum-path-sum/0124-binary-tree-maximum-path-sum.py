# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (float('-inf'), 0) # (largestSum, largestPath)

            leftMaxSum, leftGain = dfs(node.left)
            rightMaxSum, rightGain = dfs(node.right)

            leftGain = max(leftGain, 0)
            rightGain = max(rightGain, 0)
            
            largestSum = node.val + leftGain + rightGain
            largestSum = max(largestSum, rightMaxSum, leftMaxSum)
            largestPath = node.val + max(leftGain, rightGain)

            return (largestSum, largestPath)
        return dfs(root)[0]
