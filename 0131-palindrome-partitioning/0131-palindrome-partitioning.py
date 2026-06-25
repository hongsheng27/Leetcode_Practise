class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, path):
            # base case
            if start >= len(s):
                res.append(path.copy())
                return
            # recursion case
            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    path.append(s[start: end + 1])
                    backtrack(end + 1, path)
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