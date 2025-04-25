class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            if tuple(count) not in res:
                res[tuple(count)] = [word]
            else:
                res[tuple(count)].append(word)
                
        return list(res.values())