# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        p = len(postorder) - 1
        inorderIndex = {}
        for i in range(len(inorder)):
            inorderIndex[inorder[i]] = i

        def build(l, r):
            nonlocal p
            if l > r: return None
            head = TreeNode(postorder[p])
            m = inorderIndex[postorder[p]]
            p -= 1
            head.right = build(m+1,r)
            head.left = build(l,m-1)
            
            return head

        return build(0, len(inorder) - 1)