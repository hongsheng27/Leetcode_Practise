class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        for i in range(n2, -1, -1):
            base = str2[:i+1]
            if n1 % len(base): continue
            if n2 % len(base): continue

            if (base * (n1 // len(base)) == str1
                and base * (n2 // len(base)) == str2):
                return base
        return ""
