class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        buying = prices[0]
        mProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < buying:
                buying = prices[i]
            elif prices[i] - buying > mProfit:
                mProfit = prices[i] - buying

        return mProfit