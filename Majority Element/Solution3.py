# O(n), O(1)
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        res = count = 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        return res