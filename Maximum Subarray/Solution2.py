class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sum = -inf
        cur_sum = 0

        for n in nums:
            cur_sum += n

            if cur_sum > sum:
                sum = cur_sum
                
            if cur_sum < 0:
                cur_sum = 0

        return sum