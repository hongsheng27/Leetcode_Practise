# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        def build(l, r):
            if l > r: return None
            head = TreeNode(preorder[l])
            m = l + 1
            while m <= r and preorder[m] < preorder[l]:
                m += 1
            head.left = build(l+1, m - 1)
            head.right = build(m, r)
            return head
        return build(0, len(preorder) - 1)
