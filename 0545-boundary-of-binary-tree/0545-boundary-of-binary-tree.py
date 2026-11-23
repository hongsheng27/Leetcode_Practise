# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        head = [root.val]
        if not root.left and not root.right: return head
        leaf = []
        left = []
        right = []
        
        def leftDfs(node):
            if not root.left: return 
            if not node.left and not node.right:
                return
            if node != root:
                left.append(node.val)
            if node.left:
                leftDfs(node.left)
            elif node.right:
                leftDfs(node.right)
                
        def rightDfs(node):
            if not root.right: return
            if not node.left and not node.right:
                return
            if node.right:
                rightDfs(node.right)
            elif node.left:
                rightDfs(node.left)
                
            if node != root:
                right.append(node.val)
        
        def getLeaf(node):
            if not node: return
            if not node.left and not node.right:
                leaf.append(node.val)
                return
            
            getLeaf(node.left)
            getLeaf(node.right)
                
                
        leftDfs(root)
        rightDfs(root)
        getLeaf(root)
        print(head, left, leaf, right)
        return head + left + leaf + right