class Solution:
    def maxLength(self, arr: list[str]) -> int:
        res = 0
        def dfs(index, used):
            nonlocal res
            if index == len(arr):
                res = max(res, len(used))
                return
            chars = set(arr[index])
            if len(chars) == len(arr[index]) and not (used & chars):
                for c in arr[index]:
                    used.add(c)
                dfs(index + 1, used)
                for c in arr[index]:
                    used.remove(c)
           
            dfs(index + 1, used)
        dfs(0, set())
        return res