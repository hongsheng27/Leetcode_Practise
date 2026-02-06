# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p1, p2):
            # base case
            if not p1 and not p2: return True
            if not p2 or not p1 or p1.val != p2.val: return False
            
            # recursion case
            return dfs(p1.left, p2.left) and dfs(p1.right, p2.right)
        return dfs(p, q)

        