# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def dfs(left, right):
            # base case
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False

            return (left.val == right.val and
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left))
        return dfs(root.left, root.right)
        