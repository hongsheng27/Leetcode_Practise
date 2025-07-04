# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, laywer = stack.pop()
            if node:
                res = max(res, laywer)
                stack.append([node.left, laywer + 1])
                stack.append([node.right, laywer + 1]) 
        return res
