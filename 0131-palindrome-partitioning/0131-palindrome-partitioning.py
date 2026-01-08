class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    part.append(s[i: j + 1])
                    dfs(j + 1)
                    part.pop()
        def isPalindrome(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        dfs(0)
        return res
        