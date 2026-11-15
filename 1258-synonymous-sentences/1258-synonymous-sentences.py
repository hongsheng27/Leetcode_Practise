class Solution:
    def generateSentences(self, synonyms: list[list[str]], text: str) -> list[str]:
        adj = defaultdict(list)
        for first, second in synonyms:
            adj[first].append(second)
            adj[second].append(first)

        def get_synonyms(word):
            q = deque([word])
            visited = set([word])
            res = [word]
            while q:
                w = q.popleft()
                for nei in adj[w]:
                    if nei not in visited:
                        res.append(nei)
                        visited.add(nei)
                        q.append(nei)
            return res
        textList = []
        for word in text.split():
            if word in adj:
                textList.append(get_synonyms(word))
            else:
                textList.append([word])
        res = []
        def dfs(i, path):
            # basecasse
            if i == len(textList):
                res.append(" ".join(path))
                return
            for w in textList[i]:
                path.append(w)
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return sorted(res)
            