class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for price in prices:
            if price > minPrice:
                profit += price - minPrice
            minPrice = price

        return profit