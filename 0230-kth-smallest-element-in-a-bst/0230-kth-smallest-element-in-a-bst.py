# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        self.k = k
        def dfs(root):
            if not root: return 

            dfs(root.left)
            self.k -= 1
            if not self.k: 
                self.res = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.res
