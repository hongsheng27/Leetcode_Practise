# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0, 0

            left, leftDiameter = dfs(node.left)
            right, rightDiameter = dfs(node.right)
            diameter = left + right
            return max(left, right) + 1, max(diameter, leftDiameter, rightDiameter)
        return dfs(root)[1]
            