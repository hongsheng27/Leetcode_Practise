# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, target):
            if not node: return None
            
            if target < node.val:
                node.left = dfs(node.left, target)
            elif target > node.val:
                node.right = dfs(node.right, target)
            else:
                # case 1:
                if not node.left:
                    return node.right
                # case 2:
                elif not node.right:
                    return node.left
                # case 3: have both left & right
                else:
                    successor = node.right
                    while successor.left:
                        successor = successor.left
                    node.val = successor.val
                    node.right = dfs(node.right, successor.val)
                    return node
            return node
        return dfs(root, key)
        