# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(pre, ino):
            if not pre and not ino: return None
            if len(pre) == 1 and pre == ino: return TreeNode(pre[0])
            head = TreeNode(pre[0])
            m = ino.index(pre[0])

            head.left = dfs(pre[1:m + 1], ino[:m])
            head.right = dfs(pre[m + 1:], ino[m + 1:])

            return head
        return dfs(preorder, inorder)
            


            





        