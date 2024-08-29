class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0

        for p2 in range(1, len(nums)):
            if nums[p1] == 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            if nums[p1] != 0:
                p1 += 1