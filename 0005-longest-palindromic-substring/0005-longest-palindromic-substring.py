class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_left = best_right = 0
        
        def expend(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right - 1)
        
        for i in range(len(s)):
            for l, r in [(i, i), (i, i + 1)]:
                left, right = expend(l, r)
                if right - left > best_right - best_left:
                    best_left = left
                    best_right = right
        return s[best_left: best_right + 1]

        