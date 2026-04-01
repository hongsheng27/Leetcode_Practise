class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for s in strs[0]:
            res += s
            for j in range(1, len(strs)):
                if not strs[j].startswith(res):
                    return res[:-1]
        return res
