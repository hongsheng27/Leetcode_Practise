# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(node, upper, bottom):
            if not node: return True
            if not (bottom < node.val < upper): return False

            return (dfs(node.left, node.val, bottom) and 
                    dfs(node.right, upper, node.val))
            
        return dfs(root, float('inf'), float('-inf'))