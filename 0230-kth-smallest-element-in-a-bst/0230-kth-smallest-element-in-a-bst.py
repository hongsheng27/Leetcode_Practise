# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = 0
        index = 0
        def dfs(node):
            nonlocal res
            nonlocal index
            if not node: return
            dfs(node.left)
            index += 1
            if index == k:
                res = node.val
            dfs(node.right)
            
        dfs(root)
        return res