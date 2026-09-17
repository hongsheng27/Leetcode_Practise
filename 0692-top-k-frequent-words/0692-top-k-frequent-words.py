class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        unique_words = list(count)
        
        unique_words.sort(key = lambda word: (-count[word], word))
        return unique_words[:k]
        