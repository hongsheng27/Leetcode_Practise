class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for string in strs:
            board = [0] * 26
            for s in string:
                board[ord(s) - ord('a')] += 1
            board = tuple(board)
            if board not in count:
                count[board] = []
            count[board].append(string)
        return list(count.values())
        
        