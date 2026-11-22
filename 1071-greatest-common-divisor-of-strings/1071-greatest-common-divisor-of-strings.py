class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        possible = []
        for i in range(len(str2)):
            isPass = True
            for j in range(0, len(str2), i + 1):
                if str2[j:j+i+1] != str2[:i + 1]:
                    isPass = False
                    break
            if isPass: possible.append(str2[:i + 1])
        # print(possible)
        res = ""
        for p in possible:
            if len(p) > len(res):
                isPass = True
                for i in range(0, len(str1), len(p)):
                    if str1[i:i+len(p)] != p:
                        isPass = False
                        break
                if isPass: res = p
        return res
        