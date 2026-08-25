class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for s in strs:
            alphboard = [0] * 26
            for i in range(len(s)):
                alphboard[ord(s[i]) - ord('a')] += 1
            count[tuple(alphboard)].append(s)
        return list(count.values())
