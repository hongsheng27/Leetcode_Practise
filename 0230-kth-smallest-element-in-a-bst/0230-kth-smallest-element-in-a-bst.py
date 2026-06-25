# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.index = 0
        self.res = -1
        def inorder(node):
            if not node: return None
            inorder(node.left)
            self.index += 1
            if self.index == k: self.res = node.val
            inorder(node.right)
        inorder(root)
        return self.res

        