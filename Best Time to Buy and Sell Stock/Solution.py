class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Two-Pointer
        mProfit = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                mProfit = max(prices[r] - prices[l], mProfit)
            else:
                l = r

            r += 1

        return mProfit