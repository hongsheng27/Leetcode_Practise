class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for i in range(len(s)):
                freq[ord(s[i]) - ord('a')] += 1
            group[tuple(freq)].append(s)
        return list(group.values())
