class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxRes = max(nums)
        curMax = curMin = 1

        for n in nums:
            if n == 0:
                curMax = curMin = 1

            maxTemp = curMax * n
            minTemp = curMin * n

            curMax = max(maxTemp, minTemp, n)
            curMin = min(maxTemp, minTemp, n)

            maxRes = max(curMax, maxRes)

        return maxRes