class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            maxDis = 0
            for i in range(l, r + 1):
                maxDis = max(maxDis, i + nums[i])
            l = r + 1
            r = maxDis
            res += 1

        return res