# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
        if len(preorder) == 1 and preorder == inorder: return TreeNode(preorder[0])
        head = TreeNode(preorder[0])
        m = inorder.index(preorder[0])

        head.left = self.buildTree(preorder[1:m + 1], inorder[:m])
        head.right = self.buildTree(preorder[m + 1:], inorder[m + 1:])

        return head
      
            


            





        