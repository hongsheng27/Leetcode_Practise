class Solution:
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        adj = defaultdict(list)
        for first, second in synonyms:
            adj[first].append(second)
            adj[second].append(first)
        def getSynonyms(word):
            q = deque([word])
            visited = set([word])
            res = [word]
            while q:
                w = q.popleft()
                for nei in adj[w]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
                        res.append(nei)
            return res
        
        textList = [getSynonyms(w) if w in adj else [w] for w in text.split(" ")]
        res = []
        def dfs(i, path):
            if i == len(textList):
                res.append(" ".join(path))
                return
            for nei in textList[i]:
                path.append(nei)
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return sorted(res)