# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorderIndex= {}
        for i in range(len(preorder)):
            inorderIndex[inorder[i]] = i
        p = 0
        def build(l, r):
            nonlocal p
            if l > r: return None
            head = TreeNode(preorder[p])
            m = inorderIndex[preorder[p]]
            p += 1
            head.left = build(l, m - 1)
            head.right = build(m + 1, r)
            return head 
        return build(0, len(preorder) - 1)