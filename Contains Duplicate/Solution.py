class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #HashSet

        checkSet = set()

        for n in nums:
            if n in checkSet:
                return True
            checkSet.add(n)
        return False