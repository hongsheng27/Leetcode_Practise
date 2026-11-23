# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def build(preorder, inorder):
            if not preorder: 
                return None

            head = TreeNode(preorder[0])
            m = inorder.index(preorder[0])

            head.left = build(preorder[1: m+1], inorder[:m])
            head.right = build(preorder[m+1:], inorder[m + 1:])
            return head
        return build(preorder, inorder)