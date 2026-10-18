class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # shortest path => bfs to find shortest distance
        # maintain neis like, ex: hot => {"*ot": [dot, lot], "h*t": []}
        # bfs start from beginWord, => traverse through neis

        if endWord not in wordList: return 0
        wordList.append(beginWord)
        neis = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j + 1:]
                neis[pattern].append(word)
        q = deque([beginWord])
        visited = set([beginWord])
        distance = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return distance
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for nei in neis[pattern]:
                        if nei in visited: continue
                        q.append(nei)
                        visited.add(nei)
            distance += 1
        return 0
        