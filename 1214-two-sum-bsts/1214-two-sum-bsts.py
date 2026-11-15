# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode | None, root2: TreeNode | None, target: int) -> bool:
        def dfs(node, seen):
            if not node: return seen
            seen.add(target - node.val)
            left = dfs(node.left, seen)
            right = dfs(node.right, seen)
            return left | right

        def isSumTarget(node, want):
            if not node: return False
            if node.val in want: return True

            return (isSumTarget(node.left, want) or
                    isSumTarget(node.right, want))
        
        want = dfs(root1, set())
        return isSumTarget(root2, want)
        
        
        