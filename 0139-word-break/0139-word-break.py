class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i, cache):
            if i >= len(s): return True
            if i in cache: return cache[i]
            for word in wordDict:
                if s.startswith(word, i):
                    if(dfs(i + len(word), cache)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
        return dfs(0, {})

        
            
        