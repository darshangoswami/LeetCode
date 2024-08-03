# O(n), O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for n in nums:
            if n in hashMap:
                hashMap[n] += 1
            else:
                hashMap[n] = 1
        
        for n in hashMap:
            if hashMap[n] > len(nums)/2:
                return n