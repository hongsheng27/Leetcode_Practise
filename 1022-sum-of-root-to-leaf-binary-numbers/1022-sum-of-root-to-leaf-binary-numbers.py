
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        def dfs(node, path):
            if not node: return 0

            path.append(str(node.val))
            if not node.left and not node.right:
                ans = int("".join(path), 2)
                path.pop()
                return ans

            left = dfs(node.left, path)
            right = dfs(node.right, path)
            path.pop()

            return left + right

        return dfs(root, [])
        
