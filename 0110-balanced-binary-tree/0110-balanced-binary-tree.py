# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return (0, True)
            leftHeight, isLeftBalanced = dfs(node.left)
            rightHeight, isRightBalanced = dfs(node.right)
            depth = 1 + max(leftHeight, rightHeight)
            return (depth, abs(rightHeight - leftHeight) <= 1 and isLeftBalanced and isRightBalanced)
        return dfs(root)[1]
            