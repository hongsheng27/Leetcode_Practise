# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, ground, ceil):
            # base case
            if not node: return True

            # recursion case
            return (dfs(node.left, ground, node.val) and
                    dfs(node.right, node.val, ceil) and
                    ground < node.val < ceil)

        return dfs(root, float('-inf'), float('inf'))
        