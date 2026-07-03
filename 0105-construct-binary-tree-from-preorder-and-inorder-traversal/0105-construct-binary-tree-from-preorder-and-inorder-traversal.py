# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(p, i):
            # base case
            if not p and not i: return None
            # recursion case
            head = TreeNode(p[0])
            m = i.index(p[0])
            head.left = dfs(p[1: m + 1], i[:m])
            head.right = dfs(p[m + 1:], i[m + 1:])
            return head
            
        return dfs(preorder, inorder)
