# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # base case
            if not node: return (0, 0)
            # recursion case
            leftPath, leftDiameter = dfs(node.left)
            rightPath, rightDiameter = dfs(node.right)
     
            path = 1 + max(leftPath, rightPath)
            diameter = leftPath + rightPath
            diameter = max(leftDiameter, rightDiameter, diameter)
            return (path, diameter)
        return dfs(root)[1]
        