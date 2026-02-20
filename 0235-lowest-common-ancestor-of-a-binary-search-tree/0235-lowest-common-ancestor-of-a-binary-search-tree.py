# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p, q = q, p
        def dfs(node):
            if not node or not p or not q: return None
            if p.val <= node.val <= q.val:
                return node

            res = node
            if p.val < node.val and q.val < node.val:
                left = dfs(node.left)
                if left: res = left
            else:
                right = dfs(node.right)
                if right: res = right
            return res

        return dfs(root)
