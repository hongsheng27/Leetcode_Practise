# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (float('-inf'), float('-inf')) # (largestSum, largestPath)

            leftLargestSum, leftlargestPath = dfs(node.left)
            rightLargestSum, rightLargestPath = dfs(node.right)
            
            largestSum = node.val + max(0, leftlargestPath) + max(rightLargestPath, 0)
            largestSum = max(largestSum, rightLargestSum, leftLargestSum)
            largestPath = node.val + max(max(leftlargestPath, 0), max(rightLargestPath, 0))
            return (largestSum, largestPath)
        return dfs(root)[0]

        
        