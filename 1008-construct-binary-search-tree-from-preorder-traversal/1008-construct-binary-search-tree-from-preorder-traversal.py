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

            j = l + 1
            
            while j <= r and preorder[j] < preorder[l]:
                j += 1

            head.left = build(l + 1, j - 1)
            head.right = build(j, r)
            return head
        return build(0, len(preorder) - 1)