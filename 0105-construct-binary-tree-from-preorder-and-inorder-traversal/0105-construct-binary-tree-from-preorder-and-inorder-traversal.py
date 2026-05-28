# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
        self.preorderIndex = 0
        inorderIndexMap = {}
        for i in range(len(inorder)):
            inorderIndexMap[inorder[i]] = i

        def build(left, right):
            # base case
            if right < left: return None
            # recursion case
            rootVal = preorder[self.preorderIndex]
            self.preorderIndex += 1

            mid = inorderIndexMap[rootVal]
            root = TreeNode(rootVal)
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        return build(0, len(inorder) - 1)

        