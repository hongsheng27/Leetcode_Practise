# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def recursion(node, val):
            if not node: return 0
            val = val * 2 + node.val
            if not node.left and not node.right:
                return val
            return (recursion(node.left, val) + 
                    recursion(node.right, val))

        return recursion(root, 0)

