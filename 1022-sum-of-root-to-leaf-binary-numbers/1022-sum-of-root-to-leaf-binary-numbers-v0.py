# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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
            total = 0

            if not node.left and not node.right:
                binaryStirng = "".join(path)
                total = int(binaryStirng, 2)
            else:
                total += dfs(node.left, path)
                total += dfs(node.right, path)
            
            path.pop()
            return total
            
        return int(dfs(root, []))
        