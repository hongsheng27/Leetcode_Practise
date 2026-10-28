# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root: return False
        def dfs(left, right):
            if not left and not right: return True
            if not left or not right: return False
            if left.val != right.val: return False
       
            l = dfs(left.left, right.right)
            r = dfs(left.right, right.left)
            return l and r
       

        return dfs(root.left, root.right)
