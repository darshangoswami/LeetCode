class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k == 1: return max(nums)
        res = 0

        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        while k:
            res = -(heapq.heappop(maxHeap))
            k -= 1

        return res