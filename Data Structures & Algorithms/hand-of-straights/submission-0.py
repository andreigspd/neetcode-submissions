class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        freq = {}
        for x in hand:
            freq[x] = freq.get(x, 0) + 1
        hand.sort()

        for x in hand:
            if freq[x]:
                for i in range(x, x + groupSize):
                    if i not in freq or freq[i] == 0:
                        return False
                    freq[i] -= 1
        return True
