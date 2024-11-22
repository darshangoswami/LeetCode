class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            res += [cur + [n] for cur in res]
        return res