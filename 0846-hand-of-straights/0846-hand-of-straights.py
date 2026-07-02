class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if not count[h]: continue
            for i in range(groupSize):
                count[h + i] -= 1
                if count[h + i] < 0: return False
        return True
        