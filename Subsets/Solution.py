class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []

        def dfs(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return res