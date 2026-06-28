# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return (0, 0)

            leftPath, leftDiameter = dfs(node.left)
            rightPath, rightDiameter = dfs(node.right)
            diameter = leftPath + rightPath
            return max(leftPath, rightPath) + 1, max(diameter, leftDiameter, rightDiameter)
        return dfs(root)[1]
            