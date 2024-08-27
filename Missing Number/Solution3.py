class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        sumNums = len(nums) * (len(nums) + 1) // 2

        sumArr = sum(nums)

        return sumNums - sumArr 