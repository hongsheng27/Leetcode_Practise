class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        
        heapq.heapify(hand)
        count = Counter(hand)
        while hand:
            num = heapq.heappop(hand)
            if not count[num]: continue
            for i in range(num, num + groupSize):
                count[i] -= 1
                if count[i] < 0: return False
        return True