class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        count_T = {}
        for word in strs:
            count_t = {}
            for letter in word:
                if letter not in count_t:
                    count_t[letter] = 1
                else:
                    count_t[letter] += 1
            if frozenset(count_t.items()) not in count_T:
                count_T[frozenset(count_t.items())] = [word]
            else:
                count_T[frozenset(count_t.items())].append(word)
        return list(count_T.values())