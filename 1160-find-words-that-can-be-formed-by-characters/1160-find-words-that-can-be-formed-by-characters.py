class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        # make chars as count
        # traverse words, once in count then minus 1, once become negative than continue
        # otherwise, add to length
        # W of words and average length each word is k, len of chars is c
        # ts: O(c + W * k) sc(c)
        res = 0
        available = Counter(chars)
        for word in words:
            needed = Counter(word)
            isValid = True
            for char, freq in needed.items():
                if char not in available or available[char] < freq:
                    isValid = False
            if isValid: res += len(word)
        return res
                