# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode | None, root2: TreeNode | None, target: int) -> bool:
        want1 = set()
        want2 = set()
        def dfs(node1, node2):
            # base case
            if not node1 and not node2: return False
            
            node1Left = node1Right = node2Left = node2Right = None
           
            if node2:
                want1.add(target - node2.val)
                node2Left = node2.left
                node2Right = node2.right
            if node1:
                want2.add(target - node1.val)
                node1Left = node1.left
                node1Right = node1.right
            
            if ((node1 and node1.val in want1) or
                (node2 and node2.val in want2)): return True
            
            return (dfs(node1Left, node2Left) or 
                    dfs(node1Right, node2Right))
        
        return dfs(root1, root2)