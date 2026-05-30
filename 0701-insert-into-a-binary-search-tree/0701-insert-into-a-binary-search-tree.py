# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def dfs(node):
            if not node: return None
            # recursion case
            if val > node.val:
                if not dfs(node.right):
                    node.right = TreeNode(val)
            else:
                if not dfs(node.left):
                    node.left = TreeNode(val)
            return node
        return dfs(root)

        