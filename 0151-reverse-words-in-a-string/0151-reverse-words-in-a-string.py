class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        lst = s.split()
        lst = lst[::-1]
        return " ".join(lst)
        