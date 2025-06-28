# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
  
        while q:
            qLen = len(q)
            res.append(q[-1].val)
            for _ in range(qLen):
                node = q.popleft()
                if node and node.left: 
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
        return res
            
        