# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preIdx = 0
        inMap = {}
        for i in range(len(inorder)):
            inMap[inorder[i]] = i

        def build(left, right):
            # base case
            if right <= left: return None
            # recursion case
            rootVal = preorder[self.preIdx]
            self.preIdx += 1
            root = TreeNode(rootVal)
            root.left = build(left, inMap[rootVal])
            root.right = build(inMap[rootVal] + 1, right)


            return root
        return build(0, len(inorder))

        