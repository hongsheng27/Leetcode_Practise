class Solution:
    def maxLength(self, arr: list[str]) -> int:
        res = 0

        def dfs(index, used):
            nonlocal res

            res = max(res, len(used))

            for i in range(index, len(arr)):
                chars = set(arr[i])

                # arr[i] 自己就有 duplicate
                if len(chars) != len(arr[i]):
                    continue

                # 跟已經使用的 characters 衝突
                if used & chars:
                    continue

                dfs(i + 1, used | chars)

        dfs(0, set())
        return res