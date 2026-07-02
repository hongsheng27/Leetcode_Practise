class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        count = Counter(hand)
        hand.sort()
        for h in hand:
            if count[h] == 0: continue
            for i in range(h, h + groupSize):
                count[i] -= 1
                if count[i] < 0: return False
        return True
        