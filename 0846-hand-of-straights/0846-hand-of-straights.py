class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        freq = Counter(hand)
        minH = list(freq.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if freq[i]:
                    freq[i] -= 1
                else: return False
                if not freq[i]:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True



