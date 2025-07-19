class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i, n in enumerate(nums):
            if i > max_reach:
                return False
            else:
                max_reach = max(max_reach, i + nums[i])

        return True