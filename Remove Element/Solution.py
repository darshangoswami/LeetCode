class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0

        for p2 in range(len(nums)):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1

        return p1