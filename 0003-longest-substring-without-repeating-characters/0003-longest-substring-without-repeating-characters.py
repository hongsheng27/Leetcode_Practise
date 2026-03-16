class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = length = 0
        q = deque()
        for r in range(len(s)):
            while s[r] in q:
                length = max(length, len(q))
                q.popleft()
                l += 1
            q.append(s[r])
        return max(length, len(q))

        
            
        

        