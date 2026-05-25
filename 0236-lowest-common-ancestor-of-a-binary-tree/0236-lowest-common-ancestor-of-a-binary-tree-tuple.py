# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(node, p, q):
            if not node: return (None, None)

            left_p, left_q = dfs(node.left, p, q)
            right_p, right_q = dfs(node.right, p, q)

            cur_p = left_p or right_p or node == p
            cur_q = left_q or right_q or node == q

            if cur_p and cur_q and self.res is None:
                self.res = node

            return (cur_p, cur_q)

        dfs(root, p, q)
        return self.res
            
            