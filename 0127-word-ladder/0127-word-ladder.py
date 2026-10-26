class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        wordList.append(beginWord)
        neis = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neis[pattern].append(word)
        
        visit = set([beginWord])
        q = deque([beginWord])
        length = 1
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return length
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in neis[pattern]:
                        if nei not in visit:
                            q.append(nei)
                            visit.add(nei)
            length += 1
        return 0

