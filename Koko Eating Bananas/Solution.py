class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k1 = 1
        k2 = max(piles)

        while k1 <= k2:
            k = (k1 + k2) // 2
            sum = 0

            for i in range(len(piles)):
                sum += ceil(piles[i] / k)

            if sum > h:
                k1 = k + 1
            else:
                k2 = k - 1

        return k1