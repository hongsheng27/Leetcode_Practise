class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        filterText = "".join([c.lower() if c.isalnum() else " " for c in paragraph.strip()])
        print(filterText)
        bannedSet = set(banned)

        count = {}
        for word in filterText.split():
            if word in bannedSet: continue
            count[word] = count.get(word, 0) + 1

        return max(count.items(), key=lambda x:x[1])[0]