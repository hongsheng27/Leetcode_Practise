# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root: return False
       
        def dfs(node, total):
            if not node: return False
            if not node.left and not node.right and total + node.val == targetSum: 
                return True
            
            total += node.val
            left = dfs(node.left, total)
            right = dfs(node.right, total)
           
            return left or right
        return dfs(root, 0)
