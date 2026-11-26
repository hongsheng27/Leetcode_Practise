class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        tail = self.root
        for w in word:
            if w not in tail.children:
                tail.children[w] = TrieNode()
            tail = tail.children[w]
        tail.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            # base case
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dfs(index + 1, child): 
                        return True
                return False
            if ch not in node.children: return False
            return dfs(index + 1, node.children[ch])
        return dfs(0, self.root)
            

        
       

    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)