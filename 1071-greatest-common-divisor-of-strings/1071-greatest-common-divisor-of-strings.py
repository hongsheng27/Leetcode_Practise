class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        for i in range(min(n1, n2), 0, -1):
            base = str1[:i]
            if n1 % len(base) or n2 % len(base): continue

            if (base * (n1 // len(base)) == str1
                and base * (n2 // len(base)) == str2):
                return base
        return ""
