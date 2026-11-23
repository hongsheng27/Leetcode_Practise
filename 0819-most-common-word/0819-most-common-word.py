class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        normalized_str = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        words = normalized_str.split()
        count = defaultdict(int)
        bannedSet = set(banned)
        for word in words:
            if word not in bannedSet:
                 count[word] += 1
        return max(count.items(), key = lambda x: x[1])[0]