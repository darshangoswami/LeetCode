class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = count_1 = count_2 = 0

        for n in nums:
            if n == 0:
                count_0 += 1
            if n == 1:
                count_1 += 1
            if n == 2:
                count_2 += 1

        for i in range(len(nums)):
            if count_0 != 0:
                nums[i] = 0
                count_0 -= 1
            elif count_1 != 0:
                nums[i] = 1
                count_1 -= 1
            elif count_2 != 0:
                nums[i] = 2
                count_2 -= 1