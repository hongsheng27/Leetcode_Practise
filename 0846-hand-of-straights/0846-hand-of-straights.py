class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if not count[h]: continue
            for i in range(groupSize):
                if h + i not in count or count[h + i] < 1: return False
                count[h + i] -= 1
        return True
        