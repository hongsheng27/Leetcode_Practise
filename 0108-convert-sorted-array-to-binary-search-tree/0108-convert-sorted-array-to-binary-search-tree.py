# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def build(l, r):
            if l > r: return None
            m = (l + r) // 2
            head = TreeNode(nums[m])
            head.left = build(l, m - 1)
            head.right = build(m + 1, r)
            return head
        return build(0, len(nums) - 1)
        