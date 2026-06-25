# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth = 0
        self.res = 0
        def dfs(node):
            # base case
            if not node: return
            # recursion case
            dfs(node.left)
            self.kth += 1
            if self.kth == k:
                self.res = node.val
            dfs(node.right)
        dfs(root)
        return self.res

        