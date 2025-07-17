class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        else:
            nums.reverse()
            return

        swap = len(nums) - 1

        while nums[swap] <= nums[pivot]:
            swap -= 1

        nums[pivot], nums[swap] = nums[swap], nums[pivot]

        nums[pivot + 1:] = reversed(nums[pivot + 1:])

        return