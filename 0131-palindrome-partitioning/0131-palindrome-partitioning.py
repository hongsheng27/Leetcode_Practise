class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        def backtrack(l, path):
            if l >= len(s):
                res.append(path.copy())
                return
            for r in range(l, len(s)):
                if isPalindrome(l, r):
                    path.append(s[l:r + 1])
                    backtrack(r + 1, path)
                    path.pop()
        backtrack(0, [])
        return res

        