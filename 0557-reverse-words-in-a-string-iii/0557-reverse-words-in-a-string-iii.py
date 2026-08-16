class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            lst = []
            for i in range(len(word) - 1, -1, -1):
                lst.append(word[i])
            return "".join(lst)

        arr = s.split()
        lst = []
        for w in arr:
            lst.append(reverse(w))
        return " ".join(lst)

        