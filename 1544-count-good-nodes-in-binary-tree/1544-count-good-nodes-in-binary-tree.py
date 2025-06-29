# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        if not root: return self.res
        bignestNode = root.val
        def dfs(root, bignestNode):
            if not root: return None
            if bignestNode <= root.val:
                self.res += 1
            bignestNode = max(bignestNode, root.val)
            dfs(root.left, bignestNode)
            dfs(root.right, bignestNode)

        dfs(root, root.val)
        return self.res