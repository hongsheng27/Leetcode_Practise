# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def backtrack(node):
            if not node: return (0, float('-inf')) # path, sum
            leftPath, leftSum = backtrack(node.left) 
            rightPath, rightSum = backtrack(node.right)

            leftPath = max(0, leftPath)
            rightPath = max(0, rightPath)

            path = node.val + max(leftPath, rightPath, 0)
            pathSum = node.val + leftPath + rightPath
            pathSum = max(pathSum, leftSum, rightSum)
            return (path, pathSum)

        return backtrack(root)[1]
        