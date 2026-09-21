class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = longest = length = 0
        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxFreq = max(maxFreq, count[s[r]])
            while r - l + 1 - maxFreq > k:
                count[s[l]] -= 1         
                l += 1
            longest = max(longest, r - l + 1)
        return longest
            
