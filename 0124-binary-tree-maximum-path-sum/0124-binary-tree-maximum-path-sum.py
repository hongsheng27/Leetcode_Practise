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

            leftLargestSum, leftlargestPath = dfs(node.left)
            rightLargestSum, rightLargestPath = dfs(node.right)
            
            largestSum = node.val + leftlargestPath + rightLargestPath
            largestSum = max(largestSum, rightLargestSum, leftLargestSum)
            largestPath = node.val + max(leftlargestPath, rightLargestPath)
            largestPath = max(largestPath, 0)
            return (largestSum, largestPath)
        return dfs(root)[0]

        
        