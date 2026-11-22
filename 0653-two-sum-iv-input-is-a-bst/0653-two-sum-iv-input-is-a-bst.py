# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = defaultdict(int)
        def collectNums(node):
            if not node: return
            
            nums[k - node.val] += 2 if 2 * (k - node.val) == k else 1
            
            collectNums(node.left)
            collectNums(node.right)
        collectNums(root)
        
        def dfs(node):
            if not node: return False
            if node.val in nums:
                nums[node.val] -= 1
                if nums[node.val] == 0:
                    return True
            
            return (dfs(node.left) or 
                    dfs(node.right))
        return dfs(root)