class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = length = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            length = max(length, len(window))
        return length

        
            
        

        