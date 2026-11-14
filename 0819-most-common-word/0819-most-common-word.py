class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        filtered_word = "".join([c.lower() if c.isalnum() else " " for c in paragraph])
        bannedSet = set(banned)
        count = defaultdict(int)
        for word in filtered_word.split():
            if word not in bannedSet:
                count[word] += 1
        return max(count.items(), key=lambda x: x[1])[0]