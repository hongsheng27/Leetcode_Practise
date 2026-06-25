class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            # base case
            if start >= len(s):
                res.append(path.copy())
                return
            # recursion case
            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    path.append(s[start: i + 1])
                    backtrack(i + 1, path)
                    path.pop()

        def isPalindrome(l, r):
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True


        backtrack(0, [])
        return res