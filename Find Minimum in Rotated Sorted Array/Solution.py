class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[len(nums) - 1] > nums[0]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[r] > nums[mid]:
                r = mid - 1
            elif nums [r] < nums[mid]:
                l = mid + 1