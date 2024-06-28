class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0

        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 +=1 
                nums[p1] = nums[p2]

        return p1 + 1