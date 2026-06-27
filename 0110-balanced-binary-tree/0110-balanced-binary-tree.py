# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return 0, True

            leftDepth, isLeftBalanced = dfs(node.left)
            rightDepth, isRightBalanced = dfs(node.right)
            isBalanced = abs(leftDepth - rightDepth) <= 1
            return max(leftDepth, rightDepth) + 1, isBalanced and isLeftBalanced and isRightBalanced
        return dfs(root)[1]