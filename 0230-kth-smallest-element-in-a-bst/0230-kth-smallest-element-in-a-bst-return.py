class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, remaining):
            if not node:
                return None, remaining

            # left
            res, remaining = dfs(node.left, remaining)
            if res is not None:
                return res, remaining

            # self
            remaining -= 1
            if remaining == 0:
                return node.val, remaining

            # right
            return dfs(node.right, remaining)

        res, _ = dfs(root, k)
        return res