# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, k):
            if not node: return [None, k]
            # left
            res, k = dfs(node.left, k)
            if res is not None: return [res, k]
            # self
            k -= 1
            if not k:
                return [node.val, k]
            # right
            return dfs(node.right, k)
            
        res, _ = dfs(root, k)
        return res