class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(l, r, s):
            if l >= r: return 
            s[l], s[r] = s[r], s[l]
            helper(l + 1, r - 1, s)
        
        helper(0, len(s) - 1, s)
        