class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def dfs(remaining):
            if not remaining: 
                res.append(path.copy())
                return
            for i in range(1, len(remaining) + 1):
                first = remaining[:i]
                suffix = remaining[i:]
                if not isPalindrome(first): continue
                path.append(first)
                
                dfs(suffix)
                path.pop()
        def isPalindrome(string):
            l, r = 0, len(string) - 1
            while l < r:
                if string[l] == string[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        dfs(s)
        return res
        