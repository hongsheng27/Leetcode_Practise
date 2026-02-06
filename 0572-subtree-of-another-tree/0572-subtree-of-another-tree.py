# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        def isSameTree(p1, p2):
            if not p1 and not p2: return True
            if not p1 or not p2 or p1.val != p2.val: return False

            return (isSameTree(p1.left, p2.left) and
                    isSameTree(p1.right, p2.right))
        
        if isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

        