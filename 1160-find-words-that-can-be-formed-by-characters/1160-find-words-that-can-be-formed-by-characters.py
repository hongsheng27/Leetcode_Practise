class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        # make chars as count
        # traverse words, once in count then minus 1, once become negative than continue
        # otherwise, add to length
        # W of words and average length each word is k, len of chars is c
        # ts: O(c + W * k) sc(c)
        res = 0
        for word in words:
            count = Counter(chars)
            isDone = True
            for c in word:
                if c in count:
                    count[c] -= 1
                    if count[c] < 0: 
                        isDone = False
                        break
                else:
                    isDone = False
                    break
            print(word)
            if isDone:res += len(word)
        return res
                