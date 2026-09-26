# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root: return []
        res = []
        def backtrack(node, path, total):
            print(path, total)
            if not node.left and not node.right and total == targetSum:
                res.append(path.copy())
                return
            # if total > targetSum: return

            if node.left:
                path.append(node.left.val)
                backtrack(node.left, path, total + node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                backtrack(node.right, path, total + node.right.val)
                path.pop()
        backtrack(root, [root.val], root.val)
        return res

        
        