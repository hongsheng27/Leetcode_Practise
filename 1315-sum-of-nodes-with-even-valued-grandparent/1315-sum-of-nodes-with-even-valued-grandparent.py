# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode | None) -> int:
        res = 0
        def dfs(node, parent, grand):
            nonlocal res
            # base
            if not node: return
            
            if grand and grand % 2 == 0:
                res += node.val
            
            dfs(node.left, node.val, parent)
            dfs(node.right, node.val, parent)
        dfs(root, None, None)
        return res