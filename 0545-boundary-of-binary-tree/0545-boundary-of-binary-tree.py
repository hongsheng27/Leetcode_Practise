# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        head = [root.val]
        left, right, leaves = [], [], []
       
        def dfs(node, onLeft, onRight):
            if not node: return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            if onLeft: left.append(node.val)
            dfs(node.left, onLeft, onRight and not node.right)
            dfs(node.right, onLeft and not node.left, onRight)
            if onRight: right.append(node.val)


        dfs(root.left, True, False)
        dfs(root.right, False, True)
        print(head, left, leaves, right)
        return head + left + leaves + right